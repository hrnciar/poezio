.. _config:

Configuration
=============

The configuration is located in the file ``~/.config/poezio/poezio.cfg``
On its first startup, poezio will create that file (and its containing
directories) with the default configuration. You can edit that file manually
or use the :term:`/set` command to edit some of its values directly from poezio.
This file is also used to configure key bindings, but this is explained
in the :ref:`keys-page` documentation file.

That file is read at each startup and the configuration is saved when poezio
is closed.

This configuration file **requires** all global options to be in a section
named [Poezio]. Some other options can be in optional sections and will
apply only to tabs having the option’s name.

An option is formatted like this:

``option = value``

An empty value *doesn’t* mean that the default value will be used. That’s
just an empty value. To use the default value, just comment or remove the
option entirely.

Here is a list of all the available configuration options, their meaning
and their default value.

Global section options
----------------------

These options have a sense when they are in the global section. Some of
them can also be in an optional configuration section, see the next
section of this documentation.

The options here are separated thematically for convenience but they all
go into the main config section.


Security
~~~~~~~~

Options pertaining to security, such as :ref:`TLS encryption <security settings>`
and certificate validation.

.. glossary::
    :sorted:

    ca_cert_path

        **Default value:** ``[empty]``

        Path to the certificate of the Certification Authority.
        As some services may keep different certificates, it is an alternative to
        the Trust On First Use model provided by the :term:`certificate` option.
        This option is not affected by :term:`ignore_certificate` and boths checks
        may be active at the same time.

    certificate

        **Default value:** ``[empty]``

        The SHA-2 fingerprint of the SubjectPublicKeyInfo of the SSL
        certificate as a hexadecimal string, you should not touch it,
        except if know what you are doing.

        .. note:: the fingerprint was previously a fingerprint of the whole
                  certificate, while it is now only of the SubjectPublicKeyInfo,
                  which persists across LetsEncrypt renewals, and therefore
                  reduces the noise generated by the alert dialog.

     .. versionchanged:: 0.12

    ciphers

        **Default value:** ``HIGH+kEDH:HIGH+kEECDH:HIGH:!PSK:!SRP:!3DES:!aNULL``

        The TLS cipher suites allowed, in `OpenSSL format`_. Modify this if
        you know what you are doing, see the :ref:`ciphers` dedicated section
        for more details.

    default_muc_service

       **Default value:** ``[empty]``

       If specified, will be used instead of the MUC service provided by
       the user domain.

       .. versionadded:: 0.13

    force_encryption

        **Default value:** ``true``

        If set to true, all connections will use TLS by default. Only turn this to
        false if you cannot connect to your server, and do not care about your password
        or the pricacy of your communications.

    ignore_certificate

        **Default value:** ``false``

        Skip certificate validation on connection when ``true``. Useful when you are in
        anonymous mode and changing servers often. Dangerous in other cases, from a
        security perspective.



Account
~~~~~~~

Options related to account configuration, nickname…

.. glossary::
    :sorted:

    jid

        **Default value:** ``[empty]``

        Jabber identifier. Specify it only if you want to connect using an existing
        account on a server. This is optional and useful only for some features,
        like room administration or nickname registration.
        The :term:`server` option will be ignored if you specify a JID (Jabber id)
        It should be in the form nickname@server.tld or nickname@server.tld/resource

    custom_host

        **Default value:** ``[empty]``

        A custom host that will be used instead of the DNS records for the server
        (anonymous or the jid’s) defined above.
        You should not need this in a "normal" use case.

    custom_port

        **Default value:** ``[empty]``

        A custom port to use instead of the ``5222``.
        This option can be combined with :term:`custom_host`.
        You should not need this in a "normal" use case.

    default_nick

        **Default value:** ``[empty]``

        the nick you will use when joining a room with no associated nick
        If this is empty, the $USER environment variable will be used

    server

        **Default value:** ``anon.jeproteste.info``

        The server to use for anonymous authentication;
        make sure it supports anonymous authentication.

        Note that this option doesn’t do anything at all if you’re using your own JID.

    alternative_nickname

        **Default value:** ``[empty]``

        If you want poezio to join the room with an alternative nickname when
        your nickname is already in use in the room you wanted to join, put
        a non-empty value. If you don’t, poezio won't join the room
        This value will be added to your nickname to create the alternative nickname.
        For example, if you set "_", and wanted to use the nickname "john",
        your alternative nickname will be "john\_".


    keyfile

        **Default value:** ``[empty]``

        Path to a PEM private key file to use for certificate authentication
        through SASL External. If set, :term:`certfile` **MUST** be set as well
        in order to login.

    certfile

        **Default value:** ``[empty]``

        Path to a PEM certificate file to use for certificate authentication
        through SASL External. If set, :term:`keyfile` **MUST** be set as well
        in order to login.

    rooms

        **Default value:** ``[empty]``

        The rooms you will join automatically on startup, with associated
        nickname or not.

        Format : ``room@server.tld/nickname:room2@server.tld/nickname2``.

        The :term:`default_nick` option will be used if "/nickname" is not specified.

    password

        **Default value:** ``[empty]``

        A password is needed only if you specified a :term:`jid`. It will be ignored otherwise
        If you leave this empty, the password will be asked at each startup, which is recommended.

    status

        **Default value:** ``[empty]``

        The status (show) poezio will send when connecting. It can be available,
        ``dnd``, ``chat``, ``xa`` or ``away``.

        Nothing or an invalid value will mean available.

    status_message

        **Default value:** ``[empty]``

        The status message poezio will send when connecting.

    open_all_bookmarks

        **Default value:** ``false``

        If this option is set to ``true``, all remote bookmarks, even
        those that do not have autojoin, will be opened on startup.
        (the tabs without autojoin will not be joined)



Connectivity
~~~~~~~~~~~~

Options about general or chatroom connectivity. Reconnecting does not work very
well, but you will at least want to know when you get disconnected.


.. glossary::
    :sorted:

    auto_reconnect

        **Default value:** ``true``

        Auto-reconnects you when you get disconnected from the
        server. Poezio will try to reconnect forever, until it succeeds.

    connection_check_interval

        **Default value:** ``300``

        A ping is sent to the server every N seconds, N being the value of
        that option.  Change this to a low value if you want to know quickly
        when you are disconnected, and to a very high value if bandwidth
        matters so much that you can’t afford 100 bytes/minute, or if you
        don’t want to waste your battery by waking up the TCP connection too
        often.  Disable this ping altogether by setting this value to 0.

    connection_timeout_delay

        **Default value:** ``30``

        The timeout delay of the ping referenced above, 30 should really be fine, but
        if your network is really unstable, it can be set higher or lower, depending
        of your preference.

    whitespace_interval

        **Default value:** ``300``

        Interval of the whitespace keepalive sending to the server.
        ``300`` should be fine, but change it if some services have a stricter policy
        on client inactivity.

    autorejoin

        **Default value:** ``false``

        Set to true if you want to automatically rejoin the room when you're kicked.

    autorejoin_delay

        **Default value:** ``5``

        Set to the number of seconds before reconnecting after getting kicked.
        0, a negative value, or no value means you reconnect instantly.
        This option only works if autorejoin is enabled.


XMPP features
~~~~~~~~~~~~~

These options enable, disable, or allow to configure the behavior
of some non-essential XMPP features. There is a dedicated page
to understand what is :ref:`carbons <carbons-details>` or
:ref:`user activity/gaming/mood/tune <pep-details>`.

.. glossary::
    :sorted:


    enable_avatars

        **Default value:** ``true``

        Display contact avatars in the roster.

    enable_carbons

        **Default value:** ``true``

        Set this to ``false`` to disable Message Carbons (XEP-280), which allows
        transparent message delivery from and to other resources with carbons
        enabled. There should be no reason to disable this except if you encounter
        issues with your server.

    enable_smacks

        **Default value:** ``false``

        Stream Management (XEP-0198) is an extension designed to improve
        the reliability of XMPP in unreliable network conditions (such
        as mobile networks). It can however increase bandwidth usage.
        It also requires server support.

    enable_user_nick

        **Default value:** ``true``

        Set to ``false`` if you don’t want your contacts to hint you their identity.

    go_to_previous_tab_on_alt_number

       **Default value:** ``false``

       If this is set to ``true``, when Alt+x is pressed, where x is a
       number, if you are already on the tab number x, you will jump to the
       previously selected tab. Otherwise you’ll stay on the same tab.

    group_corrections

        **Default value:** ``true``

        Enable a message to “correct” (replace) another message in the display if the
        sender intended it as such. See :ref:`Message Correction <correct-feature>` for
        more information.

    synchronise_open_rooms

        **Default value:** ``true``

        If ``false``, poezio will not store the state of currently open rooms,
        so that if you leave a room and restart poezio (or start another
        client) it will reopen it.

        If ``true``, ``/join`` will create a bookmark with ``autojoin=true``,
        and ``/leave`` will remove said bookmark.

        This was previously named ``bookmark_on_join``.

    use_bookmark_method

        **Default value:** ``[empty]``

        The method that poezio will use to store your bookmarks online.
        Possible values are: ``privatexml``, ``pep``.
        You should not have to edit this in a normal use case.

    use_pep_nick

        **Default value:** ``true``

        Use the nickname broadcasted by the user if set to ``true``, and if none
        has already been set manually.

    use_remote_bookmarks

        **Default value:** ``true``

        Use this option to force the use of local bookmarks if needed.
        Anything but "false" will be counted as true.

    enable_xhtml_im

        **Default value:** ``true``

        XHTML-IM is an XMPP extension letting users send messages containing
        XHTML and CSS formatting. We can use this to make colored text for example.
        Set to ``true`` if you want to see colored (and otherwise formatted) messages.

    enable_css_parsing

        **Default value:** ``true``

        When parsing XHTML-IM content, only keep semantic elements, and not inline
        text styles.
        Only useful if :term:`enable_xhtml_im` is enabled.

    request_message_receipts

        **Default value:** ``true``

        Request message receipts when sending messages (except in groupchats).

    ack_message_receipts

        **Default value:** ``true``

        Acknowledge message receipts requested by the other party.


    send_chat_states

        **Default value:** ``true``

        if ``true``, chat states will be sent to the people you are talking to.
        Chat states are, for example, messages informing that you are composing
        a message or that you closed the tab, etc.

        Set to ``false`` if you don't want people to know these information
        Note that you won’t receive the chat states of your contacts
        if you don't send yours.


    send_os_info

        **Default value:** ``true``

        If ``true``, information about the Operation System you're using
        will be sent when requested by anyone
        Set to ``false`` if you don't want people to know these information.

        Note that this information will not be sent if :term:`send_poezio_info` is False

    send_poezio_info

        **Default value:** ``true``

        if true, information about the software (name and version)
        will be sent if requested by anyone
        Set to false if you don't want people to know these information

    send_time

        **Default value:** ``true``

        If ``true``, your current time will be sent if asked
        Set to ``false`` if you don't want people to know that information

Visual interface
~~~~~~~~~~~~~~~~

All these options will change how poezio looks, either by removing
parts of the interface, adding them, changing the ordering of stuff,
or the way messages are displayed.


.. glossary::
    :sorted:

    use_tab_nicks

        **Default value:** ``true``

        The tabs have a name, and a nick, which is, for a contact, its name in
        the contact list, or for a private conversation, the nickname in the
        chatroom. Set this to ``true`` if you want to have them shown instead
        of the jid of the contact.

    theme

        **Default value:** ``[empty]``

        The name of the theme file (without the .py extension) that will be used.
        The file should be located in the :term:`themes_dir` directory.

        If the file is not found (or no filename is specified) the default
        theme will be used instead

    themes_dir

        **Default value:** ``[empty]``

        If :term:`themes_dir` is not set, themes will searched for in
        ``$XDG_DATA_HOME/poezio/themes``, i.e. in ``~/.local/share/poezio/themes/``.
        So you should specify the directory you want to use instead.

        This directory will be created at startup if it doesn't exist

    show_composing_tabs

        **Default value:** ``direct``

        Highlight tabs where the last activity was a "composing" chat state,
        which means the contact is currently typing.

        Possible values are:

        - ``direct``: highlight only in one-to-one chats (equiv. of private & conversation)
        - ``private``: highlight only in private chats inside chatrooms
        - ``conversation``: highlight only in chats with contacts or direct JIDs
        - ``muc``: highlight only in chatrooms
        - ``true``: highlight all possible tabs (equiv. of muc & private & conversation)
        - ``false`` or any other value: don’t highlight anything

    user_list_sort

        **Default value:** ``desc``

        If set to ``desc``, the chatroom users will be displayed from top to
        bottom in the list, if set to ``asc``, they will be displayed from
        bottom to top.

    nick_color_aliases

        **Default value:** ``true``

        Automatically search for color of nick aliases. For example, if nick is
        set to red, _nick, nick\_, _nick_, nick\__ etc. will have the same color.
        Aliases colors are checked first, so that it is still possible to have
        different colors for nick\_ and nick.

    vertical_tab_list_size

        **Default value:** ``20``

        Horizontal size of the vertical tab list.

    vertical_tab_list_sort

        **Default value:** ``desc``

        If set to ``desc``, the tabs will be displayed from top to bottom in the list,
        if set to ``asc``, they will be displayed from bottom to top.

    filter_info_messages

        **Default value:** ``[empty]``

        A list of words or sentences separated by colons (":"). All the
        informational messages (described above) containing at least one of those
        values will not be shown.

    hide_exit_join

        **Default value:** ``-1``

        Exact same thing than :term:`hide_status_change`, except that it concerns
        the quit message, and that it will be hidden only if the value is ``0``.

        Default setting means:
        - all quit and join notices will be displayed

    hide_status_change

        **Default value:** ``120``

        Set a number for this setting.
        The join AND status-change notices will be
        displayed according to this number.

        ``-1``: the notices will ALWAYS be displayed

        ``0``: the notices will NEVER be displayed

        ``n``: On any other number, the notices will only be displayed
        if the user involved has talked since the last n seconds

        if the value is incorrect, ``-1`` is assumed

        Default setting means that status changes won't be displayed
        unless the user talked in the last 2 minutes

    hide_user_list

        **Default value:** ``false``

        Whether to hide the list of user in the MultiUserChat tabs or not. Useful
        for example if you want to copy/paste the content of the buffer, or if you
        want to gain space

    highlight_on

        **Default value:** ``[empty]``

        a list of words (separated by a colon (:)) that will be
        highlighted if said by someone on a room

    information_buffer_popup_on

        **Default value:** ``error roster warning help info``

        Some informational messages (error, a contact getting connected, etc)
        are sometimes added to the information buffer. These settings can make
        that buffer grow temporarily so you can read these information when they
        appear.

        A list of message types that should make the information buffer grow
        Possible values: ``error``, ``roster``, ``warning``, ``info``, ``help``

    information_buffer_type_filter

        **Default value:** ``[empty]``

        Some informational messages (error, a contact getting connected, etc)
        are sometimes added to the information buffer.

        A list of message types separated by colons (":") that should never be displayed in the information
        buffer.
        Possible values: ``error``, ``roster``, ``warning``, ``info``, ``help``

    display_user_color_in_join_part

        **Default value:** ``true``

        If set to true, the color of the nick will be used in chatroom
        information messages, instead of the default color from the theme.

    enable_vertical_tab_list

        **Default value:** ``true``

        If ``true``, a vertical list of tabs, with their name, is displayed on
        the left of the screen.  Otherwise, it is a horizontal bar with just
        the tab numbers above the input bar.

    max_nick_length

        **Default value:** ``25``

        The maximum length of the nickname that will be displayed in the
        conversation window. Nicks that are too long will be truncated and have
        a ``…`` appened to them.

    roster_group_sort

        **Default value:** ``name``

        How to sort the contact list groups. The principles are the same
        as :term:`roster_sort` (see below).

        Available methods are:
          * ``reverse``: reverse the current sorting
          * ``name``: sort by group name (alphabetical order)
          * ``fold``: sort by unfolded/folded
          * ``connected``: sort by number of connected contacts
          * ``size``: sort by group size
          * ``none``: put the "none" group (if any) at the end of the list

    roster_show_offline

        **Default value:** ``false``

        Set this to true if you want to display the offline contacts too.

    roster_sort

        **Default value:** ``jid:show``

        How you want the contacts to be sorted inside the contact list groups. The given
        methods are used sequentially (from left to right), so the last one is the
        one on the far right.

        Available methods are :

        * ``reverse``: reverse the current sorting
        * ``jid``: sort by JID (alphabetical order)
        * ``show``: sort by show (available/away/xa/…)
        * ``name``: sort by given name (if no name, then the bare jid is used)
        * ``resource``: sort by resource number
        * ``online``: sort by online presence (online or not)

        Those methods can be arranged however you like, and they have to be
        separated by colons (":"). If there are more than 3 or 4 chained
        sorting methods, your sorting is most likely inefficient.

    show_inactive_tabs

        **Default value:** ``true``

        If you want to show all the tabs in the Tab bar, even those
        with no activity, set to ``true``. Else, set to ``false``.

    show_muc_jid

        **Default value:** ``false``

        If set to ``false``, poezio will first display the bookmark name, or if
        empty the user part of the address (before the ``@``) when displaying the
        chatroom tab name. So ``poezio@muc.poez.io`` will get shortened to
        ``poezio`` unless this option is set to ``true``.
        This will be used only if :term:`use_tab_nicks` is set to ``true``.

    show_roster_jids

        **Default value:** ``true``

        Set this to ``false`` if you want to hide the JIDs in the contact list
        (and keep only the contact names). If there is no contact name, the
        JID will still be displayed.

    show_jid_in_conversations

        **Default value:** ``true``

        If ``false``, the JID of the contact will not be displayed in the information
        window in conversation tags.

    show_s2s_errors

        **Default value:** ``true``

        Show s2s errors in the contact list or not.

    show_roster_subscriptions

        **Default value:** ``[empty]``

        Select the level of display of subscriptions with a char in the contact list.

        - ``all`` to display all subscriptions
        - ``incomplete`` to display *from*, *to* and *none*
        - one of ``from``, ``to``, ``none`` and ``both`` to display only that one
        - no value or any other value to disable it

    show_tab_names

        **Default value:** ``false``

        If you want to show the tab name in the bottom Tab bar, set this to ``true``.

    unique_prefix_tab_names

        **Default value:** ``false``

        If this and :term:`show_tab_names` is set to true, only the shortest
        unique prefix of each tab name is shown instead of the full name. This
        can declutter the interface in an instance with many tabs shown in the
        interface, while not having to use numbers (which may change completely due to reordering).

        Takes precedence over `use_tab_nicks`.

    show_tab_numbers

        **Default value:** ``true``

        If you want to disable the numbers in the bottom Tab bar, set this to ``false``.
        Note that if both :term:`show_tab_names` and :term:`show_tab_numbers` are set to ``false``, the
        numbers will still be displayed.

    show_timestamps

        **Default value:** ``true``

        Whether or not to display a timestamp before each message.

    create_gaps

        **Default:** ``false``

        Create gaps when moving a tab or closing it. Enabling this option
        will help you keep the tabs at the same place during the execution of
        poezio. (gaps are not created when the closed tab is the last one)

    popup_time

        **Default value:** ``4``

        The time the message will be visible in the information buffer when it
        pops up.
        If the message takes more than one line, the popup will stay visible
        two more second per additional lines.

    muc_colors (section)

        **Default:** ``[empty]``

        Fix a color for a nick. Whenever such a nick appears in a chatroom, it
        will be displayed in that color. This color won't be changed by the
        recolor command.

User Interaction
~~~~~~~~~~~~~~~~

Options that change the behavior of poezio in a non-visual manner.

.. glossary::
    :sorted:

    add_space_after_completion

        **Default value:** ``true``

        Whether or not to add a space after a completion in the middle of the
        input (not at the start of it)

    after_completion

        **Default value:** ``,``

        What will be put after the name, when using autocompletion at the
        beginning of the input. A space will always be added after that


    beep_on

        **Default value:** ``highlight private invite disconnect``

        The terminal can beep on various event. Put the event you want in a list
        (separated by spaces).

        The events can be

        - ``highlight`` (when you are highlighted in a chatroom)
        - ``private`` (when a new private message is received, from your contacts or someone from a chatroom)
        - ``message`` (any message from a chatroom)

    separate_history

        **Default value:** ``false``

        If true, the history of inputs of the same nature won’t be shared
        between tabs (as in weechat).

    words

        **Default value:** ``[empty]``

        Personal dictionary of the words you use often, that you want to complete
        through recent words completion. They must be separated bu a colon (:). That
        completion will work in chatrooms, private conversations, and direct
        conversations.

Logging
~~~~~~~

Options related to logging.

.. glossary::
    :sorted:

    log_dir

        **Default value:** ``[empty]``

        If :term:`log_dir` is not set, logs will be saved in ``$XDG_DATA_HOME/poezio/logs``,
        i.e. in ``~/.local/share/poezio/logs/``. So, you should specify the directory
        you want to use instead. This directory will be created if it doesn't exist.

    log_errors

        **Default value:** ``true``

        Logs all the tracebacks and errors of poezio/slixmpp in
        :term:`log_dir`/errors.log by default. ``false`` disables this option.

    use_log

        **Default value:** ``true``

        Set to ``false`` if you don’t want to write any message to the disk.

Plugins
~~~~~~~

This sections references the configuration of the plugin system; for
more details, go to the :ref:`dedicated page<plugins-doc>`.

.. glossary::
    :sorted:

    plugins_autoload

        **Default value:** ``[empty]``

        Colon-separated list of plugins to load on startup.

    plugins_conf_dir

        **Default value:** ``[empty]``

        If plugins_conf_dir is not set, plugin configs will be loaded from
        :file:`$XDG_CONFIG_HOME/poezio/plugins`.
        You can specify another directory to use, it will be created if it
        does not exist.

    plugins_dir

        **Default value:** ``[empty]``

        If plugins_dir is not set, plugins will be loaded from the plugins/
        dir of the poezio install directory, then ``$XDG_DATA_HOME/poezio/plugins``.
        You can specify another directory to use. It will be created if it
        does not exist.



Other
~~~~~

.. glossary::
    :sorted:

    exec_remote

        **Default value:** ``false``

        If this is set to ``true``, poezio will try to send the commands to a FIFO
        instead of executing them locally. This is to be used in conjunction with
        ssh and the daemon.py file. See the :term:`/link` documentation for details.


    lang

        **Default value:** ``en``

        The lang some automated entities will use when replying to you.

    extract_inline_images

        **Default value:** ``true``

        Some clients send inline images in base64 inside some messages, which results in
        an useless wall of text. If this option is ``true``, then that base64 text will
        be replaced with a :file:`file://` link to the image file extracted in
        :term:`tmp_image_dir` or :file:`$XDG_CACHE_HOME/poezio/images` by default, which
        is usually :file:`~/.cache/poezio/images`

    tmp_image_dir

        **Default value:** ``[empty]``

        The directory where poezio will save the images received, if
        :term:`extract_inline_images` is set to true. If unset, poezio
        will default to :file:`$XDG_CACHE_HOME/poezio/images` which is
        usually :file:`~/.cache/poezio/images`.

    remote_fifo_path

        **Default value:** ``./``

        The path of the FIFO used to send the commands (see the :term:`exec_remote` option).
        Poezio will try to create a :file:`poezio.fifo` file in this directory.


    save_status

        **Default value:** ``true``

        Save the status automatically in the :term:`status` and :term:`status_message` options.

    send_initial_presence

        **Default value:** ``true``

        Send initial presence (normal behaviour). If ``false``, you will not send nor
        receive any presence that is not directed (through :term:`/presence`) or sent by a
        chatroom.

    lazy_resize

        **Default value:** ``true``

        Defines if all tabs are resized at the same time (if set to ``false``)
        or if they are really resized only when needed (if set to ``true``).
        ``true`` should be the most comfortable value

    max_lines_in_memory

        **Default value:** ``2048``

        Configure the number of maximum lines (for each tab) that
        can be kept in memory. If poezio consumes too much memory, lower these
        values

    max_messages_in_memory

        **Default value:** ``2048``

        Configure the number of maximum messages (for each tab) that
        can be kept in memory. If poezio consumes too much memory, lower these
        values





Optional section options
------------------------

These option can appear in optional sections. These section are named
after a JID. These option will apply only for the given JID. For example
if an option appears in a section named [user@example.com], it will
apply only for the conversations with user@example.com.

If an option appears in a section named [@example.com], it will apply
for all the conversations with people @example.com, except when the option
is already defined in a [user@example.com] section.

The priority of settings is thus like this:
user@example.com > @example.com > Poezio (more specific to less specific)

Note that some of these options can also appear in the global section,
they will be used as a fallback value when no JID-specific option is
found.

.. code-block:: ini

    [Poezio]
    foo = false
    [user@example.com]
    foo = true
    [@example.com]
    bar = false

.. glossary::
    :sorted:

    autorejoin

        **Default value:** ``false``

        Set to ``true`` if you want to automatically rejoin the
        room when you're kicked or banned.

    autorejoin_delay

        **Default value:** ``5``

        Set to the number of seconds before reconnecting after getting kicked or
        banned.
       ``0``, a negative value, or no value means instant reconnection.

        This option only works if :term:`autorejoin` is ``true``.

    disable_beep

        **Default value:** ``false``

        Disable the beeps triggered by this conversation. Works in chatroom
        tabs, private messaging tabs, and conversation tabs.

    display_activity_notifications

        **Default value:** ``false``

        If set to ``true``, notifications about the current activity of your contacts
        will be displayed in the info buffer as 'Activity' messages.

    display_gaming_notifications

        **Default value:** ``false``

        If set to ``true``, notifications about the game your are playing
        will be displayed in the info buffer as 'Gaming' messages.

    display_mood_notifications

        **Default value:** ``false``

        If set to ``true``, notifications about the mood of your contacts
        will be displayed in the info buffer as 'Mood' messages.

    display_user_color_in_join_part

        **Default value:** ``true``

        If set to ``true``, the color of the nick will be used in chatroom
        information messages, instead of the default color from the theme.

    display_tune_notifications

        **Default value:** ``false``

        If set to ``true``, notifications about the music your contacts listen to
        will be displayed in the info buffer as 'Tune' messages.

    hide_exit_join

        **Default value:** ``-1``

        Exact same thing than hide_status_change, except that it concerns
        the quit message, and that it will be hidden only if the value is 0.
        Default setting means:
        - all quit and join notices will be displayed

    hide_status_change

        **Default value:** ``120``

        Set a number for this setting.
        The join AND status-change notices will be
        displayed according to this number.

        ``-1``: the notices will ALWAYS be displayed

        ``0``: the notices will NEVER be displayed

        ``n``: On any other number, the notices will only be displayed
        if the user involved has talked since the last n seconds

        if the value is incorrect, ``-1`` is assumed
        Default setting means that status changes won't be displayed unless
        the user talked in the last 2 minutes

    highlight_on

        **Default value:** ``[empty]``

        A list of words (separated by a colon (:)) that will be
        highlighted if said by someone on a room.

    ignore_private

        **Default value:** ``false``

        Ignore private messages sent from this room.

    password

        **Default value:** ``[empty]``

        The password needed to join the room.

    eval_password

        **Default value:** [empty]

        A command which execution will retrieve the password from a password manager.

        E.g. with secret-tool and the gnome keyring:

        .. code-block:: bash

            # Storing (to do beforehand)
            secret-tool store --label="My jabber password" xmpp your@jid

            # Retrieving (this should be the value of the option)
            secret-tool lookup xmpp  your@jid

        .. note:: This will only be used if the :term:`password` option is empty.

    private_auto_response

        **Default value:** ``Not in private, please.``

        The message you want to be sent when someone tries to message you.

    send_chat_states

        **Default value:** ``true``

        Lets you disable/enable chatstates per-JID. Works in chatroom tabs,
        private messaging tabs, and normal conversation tabs.

    show_useless_separator

        **Default value:** ``true``

        If ``false``, the separator at the bottom of a chat room will not be
        displayed if no one spoke.

    use_log

        **Default value:** ``[empty]``

        Use logs for this JID or not. No value will make poezio fall back to the
        global :term:`use_log` value.

    notify_messages

        **Default value:** ``true``

        Only for chatroom tabs: if true the tab will change its color to
        notify you when a new message is received.
        You will still be notified of highlights.  Set to ``false`` if you are
        not interested in a room non-highlight notifications.

    self_ping_delay

        **Default value:** ``0``

        When this option is set to a positive value ``n``, poezio will send
        a ping request to its own nick in the chatroom every n seconds of
        inactivity (whenever no new message or presence is received from the
        chatroom for more than n seconds).  If the chatroom service does not
        respond with a successful pong within 60 seconds (that is: on an
        error of the type “not-allowed” which means the chatroom service
        doesn’t consider us to be present in that room, or on a timeout which
        probably means that the service is down), poezio will mark that
        chatroom as not joined and will try to re-join it.  This is useful to
        know when a chatroom server crashes or becomes unavailable, because
        there is no mechanism to be informed of that fact in XMPP.

        A value of at least 60 seconds is recommended, to avoid sending too
        many requests.

        When set to 0 (the default value), no ping request will be sent.


.. _OpenSSL format: https://www.openssl.org/docs/apps/ciphers.html#CIPHER_LIST_FORMAT
