Usage
=====

This chapter explains the command line options used by Aurora in more detail. 

.. code::

        --agent-name string      Set a different name for the service, the binary and other identifiers (default "aurora-agent")
    -a, --auto-reload            Automatically reload the sigma files upon detecting changes
    -c, --config string          Process default parameters from this YAML file
        --cpu-limit int          Percentage of a single CPU core that the Aurora Agent should use at most (default 100)
        --debug                  Print debugging information
        --dump-folder string     Folder where process dumps should be stored (default ".")
        --no-eventlog            Don't log matches to the Windows event log
        --install                Install Aurora Agent as a service
        --json                   Write output as JSON instead of plain text
        --license-path string    Path to the directory containing the Aurora Agent license (default "C:\\aurora")
        --log-rotate uint        How many log rotations should be retained (default 7)
        --log-size uint          At which size the log should be rotated (default 10MB)
    -l, --logfile string         Log file path
        --minimum-level Level    Report Sigma matches with rules of this level or higher (default high)
        --report-stats           Log a message about the current agent status once per hour
    -p, --rules-path strings     Paths containing the sigma files (default [C:\aurora\rules])
    -s, --sigma-config strings   Paths to the sigma configurations that should be loaded (default [C:\aurora\default-log-sources.yml,C:\aurora\etw-log-sources.yml])
        --status                 Query the status of a running Aurora Agent service
        --trace                  Print tracing information
        --udp-target string      UDP Address (as host:port) where the Aurora Agent should write its logs to
        --uninstall              Uninstall the Aurora Agent service

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

--debug
-------

This flag can be used for debugging purposes as it increases the verbosity level of the command line output.

--dump-folder 
-------------

Use to set the folder for process memory dumps created by the predefined response action ``dump``. (see chapter :doc:`Responses <./responses>`)

--no-eventlog
-------------

Disable the output to the Windows Eventlog ``Application``.

--install 
---------

See the chapter :doc:`Installation <./installation>`.

--json 
------

Formats the log lines as JSON. Applies to the log file and UDP outputs. 

--license-path 
--------------

A path to a valid license file.

Note: Event the free version named Aurora Lite requires a license file.

--log-rotate
------------

The value given after this flag sets the number of rotated log files that should be kept. 

The default is ``7``. 

--log-size
----------

The maximum number of Megabytes before a log file gets rotated.

The default is ``10``.

-l, --log-file
--------------

This sets the absolute or relative path of a text log file. The flag ``--json`` can be used to instruct Aurora to format each messages in JSON.

--minimum-level
---------------

This is the minimum Sigma rule level to report. If e.g. set to ``medium``, only Sigma rule matches with a level of ``medium``, ``high`` and ``critical`` get reported.

--report-stats
--------------

This instructs Aurora to report the agent status once per hour to the configured output channels.

-p, --rules-path
----------------

One or more paths to Sigma rules that get used by Aurora. 

If you've combined this flag with ``--install`` the files get copied to ``C:\ProgramData\Aurora Agent\rules\`` and initialized from there.

-s, --sigma-config
------------------

Sigma config files that select the log sources, channels and map field names. (see `Sigma config files <https://github.com/SigmaHQ/sigma/tree/master/tools/config>`_)

--status
--------

This flag can be used to query information from the running service.

Note: Make sure to also set ``--agent-name`` if you've set a non-standard name.

.. code:: winbatch

    C:\aurora>aurora-agent-64.exe --status

    Aurora Agent
    Version: 1.0.0
    Sigma Revision: 0.20-1442-g80d2aee9
    Uptime (in hours): 1

    Active Outputs:
    Eventlog: enabled

    Rule Statistics:
    Loaded rules: 723
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 2004511
    Events lost so far: 0
    Sigma matches: 4

This flag can be combined with the ``--json`` flag.

.. code:: json

    {
        "Parameters": {
            "SigmaFolders": [
                "C:\\ProgramData\\Aurora-Agent\\rules",
                "C:\\ProgramData\\Aurora-Agent\\myrules"
            ],
            "AutoReload": false,
            "LogFile": "",
            "LogSources": [
                "C:\\ProgramData\\Aurora-Agent\\default-log-sources.yml",
                "C:\\ProgramData\\Aurora-Agent\\etw-log-sources.yml"
            ],
            "Debug": false,
            "Trace": false,
            "EventLogging": true,
            "ReportingLevel": "high",
            "DumpFolder": "C:\\ProgramData\\Aurora-Agent\\process-dumps",
            "Json": false,
            "LicensePath": "C:\\ProgramData\\Aurora-Agent\\aurora",
            "UdpTarget": "",
            "Silent": false,
            "CpuLimit": 100,
            "ReportStats": false,
            "LogRotateCount": 0,
            "LogSize": 10485760,
            "AgentName": "aurora-agent"
        },
        "Uptime": 3828388216900,
        "Version": "1.0.0",
        "SigmaRevision": "0.20-1442-g80d2aee9",
        "LoadedRules": 723,
        "ReloadCounter": 0,
        "EventsProcessed": 2066052,
        "EventsLost": 0,
        "SigmaMatches": 4
    }

--trace
-------

A flag that produces output that is more verbose than ``--debug``.

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
