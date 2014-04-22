"""
Defines the global config instance, used to get or set (and save) values
from/to the config file.

This module has the particularity that some imports and global variables
are delayed because it would mean doing an incomplete setup of the python
loggers.

TODO: get http://bugs.python.org/issue1410680 fixed, one day, in order
to remove our ugly custom I/O methods.
"""

DEFSECTION = "Poezio"

import logging.config
import os
import sys
from gettext import gettext as _

from configparser import RawConfigParser, NoOptionError, NoSectionError
from os import environ, makedirs, path, remove
from shutil import copy2
from args import parse_args

class Config(RawConfigParser):
    """
    load/save the config to a file
    """
    def __init__(self, file_name):
        RawConfigParser.__init__(self, None)
        # make the options case sensitive
        self.optionxform = str
        self.file_name = file_name
        self.read_file()

    def read_file(self):
        try:
            RawConfigParser.read(self, self.file_name, encoding='utf-8')
        except TypeError: # python < 3.2 sucks
            RawConfigParser.read(self, self.file_name)
        # Check config integrity and fix it if it’s wrong
        for section in ('bindings', 'var'):
            if not self.has_section(section):
                self.add_section(section)

    def get(self, option, default, section=DEFSECTION):
        """
        get a value from the config but return
        a default value if it is not found
        The type of default defines the type
        returned
        """
        try:
            if type(default) == int:
                res = self.getint(option, section)
            elif type(default) == float:
                res = self.getfloat(option, section)
            elif type(default) == bool:
                res = self.getboolean(option, section)
            else:
                res = self.getstr(option, section)
        except (NoOptionError, NoSectionError, ValueError, AttributeError):
            return default
        if res is None:
            return default
        return res

    def get_by_tabname(
            self, option, default, tabname,
            fallback=True, fallback_server=True):
        """
        Try to get the value for the option. First we look in
        a section named `tabname`, if the option is not present
        in the section, we search for the global option if fallback is
        True. And we return `default` as a fallback as a last resort.
        """
        if tabname in self.sections():
            if option in self.options(tabname):
                # We go the tab-specific option
                return self.get(option, default, tabname)
        if fallback_server:
            return self.get_by_servname(tabname, option, default, fallback)
        if fallback:
            # We fallback to the global option
            return self.get(option, default)
        return default

    def get_by_servname(self, jid, option, default, fallback=True):
        """
        Try to get the value of an option for a server
        """
        server = safeJID(jid).server
        if server:
            server = '@' + server
            if server in self.sections() and option in self.options(server):
                return self.get(option, default, server)
        if fallback:
            return self.get(option, default)
        return default


    def __get(self, option, section=DEFSECTION, **kwargs):
        """
        facility for RawConfigParser.get
        """
        return RawConfigParser.get(self, section, option, **kwargs)

    def _get(self, section, conv, option, **kwargs):
        """
        Redirects RawConfigParser._get
        """
        return conv(self.__get(option, section, **kwargs))

    def getstr(self, option, section=DEFSECTION):
        """
        get a value and returns it as a string
        """
        return self.__get(option, section)

    def getint(self, option, section=DEFSECTION):
        """
        get a value and returns it as an int
        """
        return RawConfigParser.getint(self, section, option)

    def getfloat(self, option, section=DEFSECTION):
        """
        get a value and returns it as a float
        """
        return RawConfigParser.getfloat(self, section, option)

    def getboolean(self, option, section=DEFSECTION):
        """
        get a value and returns it as a boolean
        """
        return RawConfigParser.getboolean(self, section, option)

    def write_in_file(self, section, option, value):
        """
        Our own way to save write the value in the file
        Just find the right section, and then find the
        right option, and edit it.
        """
        result = self._parse_file()
        if not result:
            return False
        else:
            sections, result_lines = result

        if not section in sections:
            result_lines.append('[%s]' % section)
            result_lines.append('%s = %s' % (option, value))
        else:
            begin, end = sections[section]
            pos = find_line(result_lines, begin, end, option)

            if pos is -1:
                result_lines.insert(end, '%s = %s' % (option, value))
            else:
                result_lines[pos] = '%s = %s' % (option, value)

        return self._write_file(result_lines)

    def remove_in_file(self, section, option):
        """
        Our own way to remove an option from the file.
        """
        result = self._parse_file()
        if not result:
            return False
        else:
            sections, result_lines = result

        if not section in sections:
            log.error('Tried to remove the option %s from a non-'
                      'existing section (%s)', option, section)
            return True
        else:
            begin, end = sections[section]
            pos = find_line(result_lines, begin, end, option)

            if pos is -1:
                log.error('Tried to remove a non-existing option %s'
                          ' from section %s', option, section)
                return True
            else:
                del result_lines[pos]

        return self._write_file(result_lines)

    def _write_file(self, lines):
        """
        Write the config file, write to a temporary file
        before copying it to the final destination
        """
        try:
            prefix, file = path.split(self.file_name)
            filename = path.join(prefix, '.%s.tmp' % file)
            fd = os.fdopen(
                    os.open(
                        filename,
                        os.O_WRONLY | os.O_CREAT,
                        0o600),
                    'w')
            for line in lines:
                fd.write('%s\n' % line)
            fd.close()
            copy2(filename, self.file_name)
            remove(filename)
        except:
            success = False
            log.error('Unable to save the config file.', exc_info=True)
        else:
            success = True
        return success

    def _parse_file(self):
        """
        Parse the config file and return the list of sections with
        their start and end positions, and the lines in the file.

        Duplicate sections are preserved but ignored for the parsing.

        Returns an empty tuple if reading fails
        """
        if file_ok(self.file_name):
            try:
                with open(self.file_name, 'r', encoding='utf-8') as df:
                    lines_before = [line.strip() for line in df]
            except:
                log.error('Unable to read the config file %s',
                        self.file_name,
                        exc_info=True)
                return tuple()
        else:
            lines_before = []

        sections = {}
        duplicate_section = False
        current_section = ''
        current_line = 0

        for line in lines_before:
            if line.startswith('['):
                if not duplicate_section and current_section:
                    sections[current_section][1] = current_line

                duplicate_section = False
                current_section = line[1:-1]

                if current_section in sections:
                    log.error('Error while reading the configuration file,'
                              ' skipping until next section')
                    duplicate_section = True
                else:
                    sections[current_section] = [current_line, current_line]

            current_line += 1
        if not duplicate_section:
            sections[current_section][1] = current_line

        return (sections, lines_before)

    def set_and_save(self, option, value, section=DEFSECTION):
        """
        set the value in the configuration then save it
        to the file
        """
        # Special case for a 'toggle' value. We take the current value
        # and set the opposite. Warning if the no current value exists
        # or it is not a bool.
        if value == "toggle":
            current = self.get(option, "", section)
            if isinstance(current, bool):
                value = str(not current)
            else:
                if current.lower() == "false":
                    value = "true"
                elif current.lower() == "true":
                    value = "false"
                else:
                    return (_('Could not toggle option: %s.'
                              ' Current value is %s.') %
                                  (option, current or _("empty")),
                            'Warning')
        if self.has_section(section):
            RawConfigParser.set(self, section, option, value)
        else:
            self.add_section(section)
            RawConfigParser.set(self, section, option, value)
        if not self.write_in_file(section, option, value):
            return (_('Unable to write in the config file'), 'Error')
        return ("%s=%s" % (option, value), 'Info')

    def remove_and_save(self, option, section=DEFSECTION):
        """
        Remove an option and then save it the config file
        """
        if self.has_section(section):
            RawConfigParser.remove_option(self, section, option)
        if not self.remove_in_file(section, option):
            return (_('Unable to save the config file'), 'Error')
        return (_('Option %s deleted') % option, 'Info')

    def silent_set(self, option, value, section=DEFSECTION):
        """
        Set a value, save, and return True on success and False on failure
        """
        if self.has_section(section):
            RawConfigParser.set(self, section, option, value)
        else:
            self.add_section(section)
            RawConfigParser.set(self, section, option, value)
        return self.write_in_file(section, option, value)

    def set(self, option, value, section=DEFSECTION):
        """
        Set the value of an option temporarily
        """
        try:
            RawConfigParser.set(self, section, option, value)
        except NoSectionError:
            pass

    def to_dict(self):
        """
        Returns a dict of the form {section: {option: value, option: value}, …}
        """
        res = {}
        for section in self.sections():
            res[section] = {}
            for option in self.options(section):
                res[section][option] = self.get(option, "", section)
        return res


def find_line(lines, start, end, option):
    """
    Get the number of the line containing the option in the
    relevant part of the config file.

    Returns -1 if the option isn’t found
    """
    current = start
    for line in lines[start:end]:
        if (line.startswith('%s ' % option) or
                line.startswith('%s=' % option)):
            return current
        current += 1
    return -1

def file_ok(filepath):
    """
    Returns True if the file exists and is readable and writeable,
    False otherwise.
    """
    val = path.exists(filepath)
    val &= os.access(filepath, os.R_OK | os.W_OK)
    return bool(val)

def check_create_config_dir():
    """
    create the configuration directory if it doesn't exist
    and copy the default config in it
    """
    CONFIG_HOME = environ.get("XDG_CONFIG_HOME")
    if not CONFIG_HOME:
        CONFIG_HOME = path.join(environ.get('HOME'), '.config')
    CONFIG_PATH = path.join(CONFIG_HOME, 'poezio')

    try:
        makedirs(CONFIG_PATH)
    except OSError:
        pass
    return CONFIG_PATH

def run_cmdline_args(CONFIG_PATH):
    "Parse the command line arguments"
    global options
    options = parse_args(CONFIG_PATH)

    # Copy a default file if none exists
    if not path.isfile(options.filename):
        default = path.join(path.dirname(__file__),
                            '../data/default_config.cfg')
        other = path.join(path.dirname(__file__), 'default_config.cfg')
        if path.isfile(default):
            copy2(default, options.filename)
        elif path.isfile(other):
            copy2(other, options.filename)
        global firstrun
        firstrun = True

def create_global_config():
    "Create the global config object, or crash"
    try:
        global config
        config = Config(options.filename)
    except:
        import traceback
        sys.stderr.write('Poezio was unable to read or'
                         ' parse the config file.\n')
        traceback.print_exc(limit=0)
        sys.exit(1)

def check_create_log_dir():
    "Create the poezio logging directory if it doesn’t exist"
    global LOG_DIR
    LOG_DIR = config.get('log_dir', '')

    if not LOG_DIR:

        data_dir = environ.get('XDG_DATA_HOME')
        if not data_dir:
            home = environ.get('HOME')
            data_dir = path.join(home, '.local', 'share')

        LOG_DIR = path.join(data_dir, 'poezio')

    LOG_DIR = path.expanduser(LOG_DIR)

    try:
        makedirs(LOG_DIR)
    except:
        pass

def setup_logging():
    "Change the logging config according to the cmdline options and config"
    if config.get('log_errors', True):
        LOGGING_CONFIG['root']['handlers'].append('error')
        LOGGING_CONFIG['handlers']['error'] = {
                'level': 'ERROR',
                'class': 'logging.FileHandler',
                'filename': path.join(LOG_DIR, 'errors.log'),
                'formatter': 'simple',
            }

    if options.debug:
        LOGGING_CONFIG['root']['handlers'].append('debug')
        LOGGING_CONFIG['handlers']['debug'] = {
                'level':'DEBUG',
                'class':'logging.FileHandler',
                'filename': options.debug,
                'formatter': 'simple',
            }


    if LOGGING_CONFIG['root']['handlers']:
        logging.config.dictConfig(LOGGING_CONFIG)
    else:
        logging.basicConfig(level=logging.CRITICAL)

    global log
    log = logging.getLogger(__name__)

def post_logging_setup():
    # common imports sleekxmpp, which creates then its loggers, so
    # it needs to be after logger configuration
    from common import safeJID as JID
    global safeJID
    safeJID = JID

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s:%(module)s:%(message)s'
        }
    },
    'handlers': {
    },
    'root': {
            'handlers': [],
            'propagate': True,
            'level': 'DEBUG',
    }
}

# True if this is the first run, in this case we will display
# some help in the info buffer
firstrun = False

# Global config object. Is setup in poezio.py
config = None

# The logger object for this module
log = None

# The command-line options
options = None

# delayed import from common.py
safeJID = None

# the global log dir
LOG_DIR = ''
