Usage
=====

This chapter explains the command line options used by Aurora in more detail. 

Run Aurora
----------

If you simply run Aurora in your terminal, it'll use the default values for each flag and no dedicated config file. 

.. code:: winbatch
    
    aurora-agent-64.exe

An existing config file can be used with the respective flag. 

.. code:: winbatch
    
    aurora-agent-64.exe -c agent-config-reduced.yml

A typical command line that runs Aurora and prints messages and matches to the command line and the Windows ``Application`` eventlog looks like this:

.. code:: winbatch 

    aurora-agent-64.exe --minimum-level low

Run Aurora as Service
---------------------

To install Aurora as a service, use the ``--install`` flag and see the chapter :doc:`installation </usage/installation>` for more details.

Command Line Flags
------------------

.. code:: none

        ___                                  ___                    __
       /   | __  ___________  _________ _   /   | ____ ____  ____  / /_
      / /| |/ / / / ___/ __ \/ ___/ __ `/  / /| |/ __ `/ _ \/ __ \/ __/
     / ___ / /_/ / /  / /_/ / /  / /_/ /  / ___ / /_/ /  __/ / / / /_
    /_/  |_\__,_/_/   \____/_/   \__,_/  /_/  |_\__, /\___/_/ /_/\__/
                                               /____/

    Aurora Agent Version 0.2.0 (b365ca69), Sigma Revision 0.20-2182-g9a96b77f1
    (C) Nextron Systems GmbH, 2021

    Usage of aurora-agent-64.exe:
          --activate-module strings             Activate the given modules, even if they are disabled by default (default [])
          --activate-responses                  Execute responses that are specified in sigma rules (e.g. to kill a process)
          --agent-name string                   Set a different name for the service, the binary and other identifiers (default "aurora-agent")
      -a, --auto-reload                         Automatically reload the sigma rules and configurations upon detecting changes
      -c, --config string                       Process default parameters from this YAML file
          --cpu-limit int                       CPU usage (as percentage) that the Aurora Agent should use at most (default 70)
          --deactivate-all-modules              Deactivate all modules, except for those specified by --activate-module
          --deactivate-module strings           Deactivate the given modules (default [])
          --debug                               Print debugging information
          --dump-folder string                  Folder where process dumps should be stored (default ".")
          --false-positive-filter-file string   Path to a file containing false positive regexes (one per line)
          --install                             Install Aurora Agent as a service
          --ioc-path strings                    Folders containing IOC files (default [signatures\iocs])
          --json                                Write output as JSON instead of plain text
          --license-path string                 Path to the directory containing the Aurora Agent license (default ".")
          --log-rotate uint                     How many log rotations should be retained (default 7)
          --log-size string                     Maximum file size for the log file. It will be rotated once it exceeds this. (default "10MB")
      -s, --log-source strings                  Paths to the sigma log sources that should be loaded (default [log-sources\event-log-sources.yml,log-sources\etw-log-sources-standard.yml,log-sources\etw-log-source-mappings.yml])
      -l, --logfile string                      Log file path
          --low-prio                            Run Aurora Agent with low process priority
          --match-burst uint                    Number of matches for a single rule that are allowed to exceed the throttling for a short time (default 5)
          --match-throttling string             Minimum average time between matches. Sigma Rules with responses will ignore this setting. (default "1m")
          --minimum-level Level                 Report Sigma matches with rules of this level or higher (default medium)
          --module-info                         List all available modules
          --no-content-enrichment               Deactivate calculations that rely on disk access (e.g. hashes) for executables and DLLs in important events
          --no-eventlog                         Don't log matches to the Windows event log
          --no-stdout                           Disable logging to the standard output
          --output-throttling string            minimum average time between log messages (warning: if set, it can cause Aurora Agent to drop messages if many matches occur!) (default "0h")
          --print-event-id                      Print the Event ID that Aurora would assign when logging to the Eventlog as part of each message
          --report-stats                        Log a message about the current agent status regularly
          --report-stats-interval string        Interval between status messages, see --report-stats (default "1h")
      -p, --rules-path strings                  Paths containing the sigma files (default [signatures\sigma-rules])
          --status                              Query the status of a running Aurora Agent service
          --tcp-target string                   TCP Address (as host:port) where the Aurora Agent should write its logs to
          --trace                               Print tracing information. This generates a very high number of events per second.
          --udp-target string                   UDP Address (as host:port) where the Aurora Agent should write its logs to
          --uninstall                           Uninstall the Aurora Agent service
          --version                             Show Aurora Agent version

--activate-module
-----------------

This flag is used to explicitly activate certain modules. To get an overview of the available modules, use the ``--module-info`` flag.

--activate-responses
--------------------

This flag enables response actions in the agent. Without setting this flag to ``true``, Aurora will not perform any response action even if response actions are defined in one or more rules. 

The default is ``false``. 

--agent-name
------------

It's possible to set a different name for the service name, the binary name on disk and other unique identifiers used by the agent.

This feature provides a basic way to hide Aurora on an end system.

-a, --auto-reload
-----------------

By setting the ``auto-reload`` flag, Aurora monitors the rules folders for changes and applies them every ``10`` seconds.

-c, --config
------------

A config or config template can be set with the ``--config`` flag. If you use this flag combined with the ``--install`` flag, it will use all configured parameters in the file and write the new config file to the program folder.

--cpu-limit
-----------

This flag allows to set a CPU usage limit from 1 to 100. Aurora uses only one CPU core and applies that limit to its activity on this single core. 

WARNING: by setting a low CPU limit, it becomes more likely that events get dropped. Use the ``--status`` or ``--report-stats`` flag to monitor the number of dropped events.

--deactivate-all-modules
------------------------

This flag deactivates all modules in Aurora that are not explicitly enabled with ``--activate-module``. It can be used to debug issues with specific modules.

--deactivate-module
-------------------

This deactivates certain modules in Aurora. To get an information on the available modules use the ``--module-info`` flag.

--debug
-------

This flag can be used for debugging purposes as it increases the verbosity level of the command line output.

--dump-folder 
-------------

Use to set the folder for process memory dumps created by the predefined response action ``dump``. (see chapter :doc:`Responses <./responses>`)

--false-positive-filter-file
----------------------------
Requires a path to file containing one regular expression per line. Log lines that match any regular expression are suppressed.

--ioc-path
----------
Path to the directories containing IOCs for Aurora. (see chapter :doc:`Configuration <./configuration>`)

--install 
---------

See the chapter :doc:`Installation <./installation>`.

--json 
------

Formats the log lines as JSON. Applies to all outputs except for the Windows Eventlog.

--license-path 
--------------

A path to a valid license file.

Note: Even the free version named Aurora Lite requires a license file.

--log-rotate
------------

The value given after this flag sets the number of rotated log files that should be kept. 

The default is ``7``. 

--log-size
----------

The maximum size of a log file before it is rotated.

The default is ``10MB``. Supported units are ``B``, ``KB``, ``MB``, and ``GB``.

-s, --log-source
------------------

Paths to the sigma configs that should be loaded. Sigma config files are files that select the log sources, channels and map field names. 
(see `Sigma config files <https://github.com/SigmaHQ/sigma/tree/master/tools/config>`_)

-l, --log-file
--------------

This sets the absolute or relative path of a text log file. The flag ``--json`` can be used to instruct Aurora to format each messages in JSON.

--low-prio
----------

Run Aurora Agent with low process priority.

--match-burst
-------------
Number of matches for a single rule that are allowed to exceed the throttling for a short time.

(default 5)

--match-throttling
------------------

Minimum average time between matches. Sigma Rules with responses will ignore this setting. 

(default "1m")

--minimum-level
---------------

This is the minimum Sigma rule level to report. If e.g. set to ``medium``, only Sigma rule matches with a level of ``medium``, ``high`` and ``critical`` get reported.

--module-info 
-------------

Prints information on the available detection modules. (Aurora Lite only supports the Sigma matching)

--no-content-enrichment
-----------------------

Deactivate calculations that rely on disk access (e.g. hashes) for executables and DLLs in important events

--no-eventlog
-------------

This flag disables the output to the local ``Application`` event log.

--no-stdout
-------------

This flag disables the output to the standard output.

--output-throttling
-------------------

Minimum average time between log messages (default "0h")

Supported units are ``s`` (seconds), ``m`` (minutes) and ``h`` (hours).

WARNING: by setting a maximum event output, it becomes more likely that events get dropped. Use the ``--status`` or ``--report-stats`` flag to monitor the number of dropped events.

-p, --rules-path
----------------

One or more paths to Sigma rules that get used by Aurora. 

If you've combined this flag with ``--install`` the files get copied to ``C:\ProgramData\Aurora Agent\rules\`` and initialized from there.

--print-event-id
----------------

Print the Event ID that Aurora would assign when logging to the Eventlog as part of each message

--report-stats
--------------

Instructs Aurora to write a status message every X minutes into the defined output channels.

Default is ``false``. 

--report-stats-interval
-----------------------

Sets an interval for the status messages that get written into the defined output channels. Requires ``--report-stats``. 

Default is ``1h``. Supported units are ``s`` (seconds), ``m`` (minutes) and ``h`` (hours).

--status
--------

This flag can be used to query status information from the running service.

Note: Make sure to also set ``--agent-name`` if you've set a non-standard name.

This flag can be combined with the ``--json`` and ``--trace`` flags for JSON formatted or more detailed output.

Status information will include information about: 

- Loaded sigma rules
- Observed events
- Sigma matches
- Active outputs

--tcp-target
------------

This flag defines a remote system to which the log data gets send via TCP. 

.. code:: winbatch 

    aurora-agent-64.exe --tcp-target our-siem.company.net:5001

--trace
-------

A flag that produces output that is more verbose than ``--debug``.

In most cases it is recommended to redirect the output of this command into a file, which you can review later. Otherwise the terminal gets flooded with event messages (often more than 1000 per second).

.. code:: winbatch

    aurora-agent-64.exe --trace > d:\aurora-trace.log

--udp-target
------------

This flag defines a remote system to which the log data gets send via UDP. 

.. code:: winbatch 

    aurora-agent-64.exe --udp-target our-siem.company.net:5001

.. code:: winbatch 

    aurora-agent-64.exe --udp-target 10.0.3.101:888

You can combine this flag with the ``--json`` flag to format the output in JSON. 

--uninstall
-----------

Use this flag to uninstall Aurora. 

Note: Make sure to also set ``--agent-name`` if you've set a non-standard name.

--version
---------

Print Aurora Agent version
