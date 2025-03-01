#!/usr/bin/env python3
import os
import subprocess
import sys
from tempfile import TemporaryFile

try:
    from setuptools import setup, Extension
except ImportError:
    print('\nSetuptools was not found. Install setuptools for python 3.\n')
    sys.exit(1)

cmdclass = {}
try:
    from sphinx.setup_command import BuildDoc
    cmdclass = {'build_man': BuildDoc}
except ImportError:
    print('\nSphinx not found, the build_man command will be unavailable.\n')

current_dir = os.path.dirname(__file__)

from poezio.version import __version__

def get_relative_dir(folder, stopper):
    """
    Find the path from a directory to a pseudo-root in order to recreate
    the filetree.
    """
    acc = []
    last = os.path.basename(folder)
    while last != stopper:
        acc.append(last)
        folder = os.path.dirname(folder)
        last = os.path.basename(folder)
    return os.path.join(*acc[::-1]) if acc else ''

def find_doc(before, path):
    _files = []
    stop = os.path.basename(path)
    for root, dirs, files in os.walk(os.path.join(current_dir, 'doc', path)):
        files_path = []
        relative_root = get_relative_dir(root, stop)
        for name in files:
            files_path.append(os.path.join(root, name))
        _files.append((os.path.join(before, relative_root), files_path))
    return _files

def check_include(library_name, header):
    command = [os.environ.get('PKG_CONFIG', 'pkg-config'), '--cflags', library_name]
    try:
        cflags = subprocess.check_output(command).decode('utf-8').split()
    except FileNotFoundError:
        print('pkg-config not found.')
        return False
    except subprocess.CalledProcessError:
        # pkg-config already prints the missing libraries on stderr.
        return False
    command = [os.environ.get('CC', 'cc')] + cflags + ['-E', '-']
    with TemporaryFile('w+') as c_file:
        c_file.write('#include <%s>' % header)
        c_file.seek(0)
        try:
            return subprocess.call(command, stdin=c_file, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0
        except FileNotFoundError:
            print('%s headers not found.' % library_name)
            return False

def sphinx_man():
    expected_sphinx_files = [
        'build/sphinx/man/poezio.cfg.7',
        'build/sphinx/man/poezio.keys.7',
        'build/sphinx/man/poezio.commands.7'
    ]
    found = []
    for item in expected_sphinx_files:
        if os.path.exists(item):
            found.append(item)
    if found:
        return [('share/man/man7/', found)]
    return []


sphinx_files_found = sphinx_man()
if not sphinx_files_found:
    print(
        '\nSphinx-built manpages not found. Only the '
        'short handwritten manpages will be installed\n'
    )


if not check_include('python3', 'Python.h'):
    sys.exit(2)

module_poopt = Extension('poezio.poopt',
                    extra_compile_args=['-Wno-declaration-after-statement'],
                    sources=['poezio/pooptmodule.c'])

# Create a link to the config file (for packaging purposes)
if not os.path.exists(os.path.join(current_dir, 'poezio', 'default_config.cfg')):
    os.link(os.path.join(current_dir, 'data', 'default_config.cfg'),
         os.path.join(current_dir, 'poezio', 'default_config.cfg'))

# identify the git version
git_dir = os.path.join(current_dir, '.git')
if os.path.exists(git_dir):
    try:
        result = subprocess.Popen(['git', '--git-dir', git_dir, 'describe'],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL)
        result.wait()
        data = result.stdout.read().decode('utf-8', errors='ignore')
        version = '.dev' + data.split('-')[1]
    except:
        version = '.dev1'
else:
    version = ''

with open('README.rst', encoding='utf-8') as readme_fd:
    LONG_DESCRIPTION = readme_fd.read()

setup(
    name="poezio",
    version=__version__ + version,
    description="A console XMPP client",
    long_description=LONG_DESCRIPTION,
    ext_modules=[module_poopt],
    url='https://poez.io/',
    license='zlib',
    download_url='https://poez.io/#download',

    author='Florent Le Coz',
    author_email='louiz@louiz.org',

    maintainer='Mathieu Pasquet',
    maintainer_email='mathieui@mathieui.net',

    classifiers=['Development Status :: 5 - Production/Stable',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: XMPP',
        'Environment :: Console :: Curses',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: zlib/libpng License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only'],
    keywords=['jabber', 'xmpp', 'client', 'chat', 'im', 'console'],
    packages=['poezio', 'poezio.core', 'poezio.tabs', 'poezio.windows',
        'poezio.ui', 'poezio_plugins', 'poezio_themes'],
    package_dir={'poezio': 'poezio',
        'poezio_plugins': 'plugins',
        'poezio_themes': 'data/themes'},
    package_data={'poezio': ['default_config.cfg']},
    scripts=['scripts/poezio_logs'],
    entry_points={'console_scripts': ['poezio = poezio.__main__:run']},
    data_files=([
            ('share/man/man1/', ['data/poezio.1', 'data/poezio_logs.1']),
            ('share/poezio/', ['README.rst', 'COPYING', 'CHANGELOG']),
            ('share/applications/', ['data/io.poez.Poezio.desktop']),
            ('share/metainfo/', ['data/io.poez.Poezio.appdata.xml'])
        ]
        + find_doc('share/doc/poezio/source', 'source')
        + find_doc('share/doc/poezio/html', 'build/html')
        + sphinx_files_found
    ),
    install_requires=['slixmpp>=1.6.0', 'aiodns', 'pyasn1_modules', 'pyasn1', 'typing_extensions'],
    extras_require={'OTR plugin': 'python-potr>=1.0',
        'Screen autoaway plugin': 'pyinotify==0.9.4',
        'Avoiding cython': 'cffi'},
    cmdclass=cmdclass,
    command_options={
        'build_man' : {
            'builder': ('setup.py', 'man'),
        }
    },
)

# Remove the link afterwards
if (os.path.exists(os.path.join(current_dir, 'poezio', 'default_config.cfg')) and
        os.path.exists(os.path.join(current_dir, 'data', 'default_config.cfg'))):

    os.unlink(os.path.join(current_dir, 'poezio', 'default_config.cfg'))

