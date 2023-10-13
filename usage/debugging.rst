Debugging
=========

The best way to debug Aurora is to run it directly in the command line and don't use it as service. 

.. code:: winbatch

    aurora-agent-64.exe --debug

The verbosity can even be increased by using the ``--trace`` flag. 

Status Information
------------------

The ``--status`` can give you information from a running Aurora service.

.. code:: none

    C:\aurora>aurora-agent-64.exe --status
    Aurora Agent
    Version: 0.1.6
    Build Revision: 5fef68a1
    Sigma Revision: 0.20-1884-ga4a26540
    Status: running
    Uptime (in hours): 0

    Active Outputs:
    Eventlog: enabled
    Stdout: enabled

    Rule Statistics:
    Loaded rules: 734
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 89419
    Events lost so far: 0
    Sigma matches: 4
    Suppressed Sigma matches of those: 0

    Response Actions: disabled

It displays the number of events that the agent was able to see and process, the number of initialized rules and rule matches. 

Adding the flag ``--trace`` includes more information in the output, e.g. the number of processed events per ETW event channel.

.. code:: none

    C:\aurora\>aurora-agent-64.exe --status --trace
    Aurora Agent
    Version: 0.1.6
    Build Revision: 5fef68a1
    Sigma Revision: 0.20-1884-ga4a26540
    Status: running
    Uptime (in hours): 0

    Active Outputs:
    Eventlog: enabled
    Stdout: enabled

    Rule Statistics:
    Loaded rules: 734
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 111138
            88650 events from WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
            20094 events from WinEventLog:Microsoft-Antimalware-Engine
            1265 events from PollNamedPipes
            400 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_IMAGE
            306 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_PROCESS
            174 events from WinEventLog:Microsoft-Windows-Kernel-Registry/CreateKey
            164 events from SystemLogger:Process
            46 events from WinEventLog:Microsoft-Windows-DNS-Client
            19 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_CREATE_NEW_FILE
            11 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_DELETE_PATH
            9 events from WinEventLog:Microsoft-Windows-TCPIP/ut:ConnectPath
    Events lost so far: 0
    Sigma matches: 4
            Run Whoami Showing Privileges: 2
            Suspicious Certutil Command: 2
    Suppressed Sigma matches of those: 0

    Response Actions: disabled

The JSON output includes all the information plus the agent configuration settings. 

.. code:: none

    C:\aurora\>aurora-agent-64.exe --status --json
    {
            "Parameters": {
                    "SigmaFolders": [
                            "C:\\aurora\\rules"
                    ],
                    "AutoReload": false,
                    "LogFile": "",
                    "LogSources": [
                            "log-sources\\etw-log-sources-standard.yml"
                    ],
                    "Debug": false,
                    "Trace": false,
                    "NoEventlog": false,
                    "ReportingLevel": "high",
                    "Json": false,
                    "LicensePath": "C:\\aurora\\",
                    "UdpTarget": "",
                    "Silent": false,
                    "CpuLimit": 100,
                    "ReportStats": false,
                    "ReportStatsInterval": 3600000000000,
                    "LogRotateCount": 7,
                    "LogSize": 10485760,
                    "AgentName": "aurora-agent",
                    "ActivateModules": null,
                    "DeactivateModules": null,
                    "NoStdout": false,
                    "EventThrottling": 0,
                    "LowPrio": false,
                    "PrintEventId": false,
                    "ConsumerParameters": {
                            "ActivateResponses": false,
                            "DumpFolder": ".",
                            "SigmaMatchThrottling": 60000000000,
                            "SigmaMatchBurst": 5
                    },
                    "ProviderParameters": {
                            "NoHashes": false
                    }
            },
            "Uptime": 334601989600,
            "Version": "0.1.6",
            "SigmaRevision": "0.20-1884-ga4a26540",
            "BuildRevision": "5fef68a1",
            "CurrentAction": "running",
            "LoadedRules": 734,
            "ReloadCounter": 0,
            "EventsProcessed": {
                    "PollNamedPipes": 1815,
                    "SystemLogger:Process": 175,
                    "WinEventLog:Microsoft-Antimalware-Engine": 27847,
                    "WinEventLog:Microsoft-Windows-DNS-Client": 57,
                    "WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls": 124269,
                    "WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_CREATE_NEW_FILE": 22,
                    "WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_DELETE_PATH": 11,
                    "WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_IMAGE": 645,
                    "WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_PROCESS": 314,
                    "WinEventLog:Microsoft-Windows-Kernel-Registry/CreateKey": 342,
                    "WinEventLog:Microsoft-Windows-TCPIP/ut:ConnectPath": 26
            },
            "EventsLost": 0,
            "SigmaMatches": {
                    "Run Whoami Showing Privileges": 2,
                    "Suspicious Certutil Command": 2
            },
            "SuppressedSigmaMatches": {},
            "ActiveModules": null
    }


Diagnostic information
----------------------

Diagnostic pack
^^^^^^^^^^^^^^^

You can create a diagnostic pack to detect and debug performance problems.

Simply run:

.. code:: none 

    .\aurora-agent-util.exe diagnostics

This creates a ZIP file with debugging information (such as heap usage, stack traces, ...)
that we can use to analyze these issues.

Profiling server
^^^^^^^^^^^^^^^^

If Aurora has been started with ``--pprof``, information can also be gathered manually via a web interface: 

.. code:: winbatch 

    curl.exe http://localhost:8080/debug/pprof/profile?seconds=20 --output aurora-debug.pprof
    curl.exe http://localhost:8080/debug/pprof/heap --output aurora-heap.pprof
    curl.exe http://localhost:8080/debug/pprof/goroutine --output aurora-stack-traces.pprof

This is the same information that is included in the diagnostic pack.

Crashes 
-------

In cases of unexpected crashes, the following command lines can help you identify the source of the problem. 

.. code:: none 

    C:\Program Files\Aurora Agent\>aurora-agent.exe -c agent-config.yml > aurora-crash.log 2>&1

.. code:: none 

    C:\Program Files\Aurora Agent\>aurora-agent.exe -c agent-config.yml --trace > aurora-crash-trace.log 2>&1

Error Messages
--------------

Check the configured log outputs for error messages. A faulty rule would e.g. lead to error messages like this one in the ``Application`` eventlog with EventID 

.. code:: none

    Could not reload sigma rules 
    Module: Aurora-Agent 
    Changed_files: C:\Program Files\Aurora-Agent\myrules\my-ransomware.yml 
    Error: could not parse rule response in file "C:\\Program Files\\Aurora-Agent\\myrules\\my-ransomware.yml": invalid predefined response action kil 

Performance Tuning
------------------

Event Source Tuning
^^^^^^^^^^^^^^^^^^^

Event Sources and Consumers
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Internally, Aurora has a number of event consumers. The event consumers are: 

- Aurora's built-in modules
- Sigma log sources

Each event consumer consists of: 

- A number of requested event sources
- Logic to handle incoming events from these sources

Performance is primarily determined by the number of incoming events that Aurora has to process;
The impact of Sigma rule matching, in comparison, is fairly low.

Therefore, to optimize performance, choose your event sources wisely and avoid event sources that
produce an extreme number of events.

Event Source Analysis
~~~~~~~~~~~~~~~~~~~~~

When executing ``aurora-agent.exe --status --trace`` while Aurora is running, an overview
of events that was received for each event source is generated. The performance impact of each source
scales roughly linear with the number of events.

To see which built-in modules requests which event source, the requested log sources can be listed with 
``aurora-agent.exe --module-info --trace``. 

For sigma log sources, inspect the sigma configurations that are used by Aurora. 
By default, ``etw-log-sources.yml`` and ``default-log-sources.yml`` from the Aurora directory are used.

Each sigma log source in these files that has a ``sources`` element requests the event sources listed
in that element.

Event Source Definitions
~~~~~~~~~~~~~~~~~~~~~~~~
Aurora Agent supports the following event source prefixes:

- ``WinEventLog:`` Events from an Eventlog channel or ETW provider. 

  The schema for these sources is: ``WinEventLog:Provider/Channel?Options``

  Channels and options are optional and add further restrictions on events from the provider that is
  requested.
  A full list of Eventlog channels on a system can be found using the Event Viewer. A full list of ETW providers on a system
  can be found using e.g. https://github.com/zodiacon/EtwExplorer.
- ``SystemLogger:`` Events from the System Trace Provider
  (see https://docs.microsoft.com/en-us/windows/win32/etw/configuring-and-starting-a-systemtraceprovider-session for details).

  The schema is: ``SystemLogger:SystemLoggerFlag`` where the supported ``SystemLoggerFlag`` flags are:

  - FileIO
  - Process
  - Thread
  - Registry
  - Image
  - Network-TCP-IP
  - Handle
- ``PollHandles``: This event source is handled by a provider in Aurora that regularly creates an event for each handle that exists on a system.

Example: Disabling a Noisy Log Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this example, say that ``aurora-agent.exe --status --trace`` results in this event overview:

.. code:: none

   Events observed so far: 50657
        36783 events from WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
        7611 events from WinEventLog:Microsoft-Windows-Kernel-File?eventids=14
        1842 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_IMAGE
        1273 events from WinEventLog:Microsoft-Windows-Kernel-Registry/CreateKey
        1058 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_THREAD
        995 events from WinEventLog:Microsoft-Windows-DNS-Client
        585 events from PollNamedPipes
        235 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_FILENAME
        169 events from SystemLogger:Process
        39 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_CREATE_NEW_FILE
        32 events from WinEventLog:Microsoft-Windows-Sysmon/Operational
        22 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_PROCESS
        5 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_DELETE_PATH
        3 events from WinEventLog:Security
        3 events from WinEventLog:Application
        2 events from WinEventLog:Microsoft-Windows-Kernel-Registry/DeleteKey

As we can see, the by far noisiest event source is ``WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls``.

If we want to disable this event source to lessen Aurora's CPU usage, we must find the event consumers that request
it.

``aurora-agent.exe --module-info --trace`` shows these modules which use this event source:

.. code:: none

   Aurora Agent Modules:
        LsassDumpCheck
                Requested sources:
                ...
                WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
        Beaconhunter
                Requested sources:
                ...
                WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
                ...

Searching in ``etw-log-sources.yml``, we find that there is also a Sigma log source definition which uses this event source: 

.. code:: yaml

   windows-api-call-auditing:
      product: windows
      service: api-call-auditing
      sources:
         - "WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls"

To deactivate this log source, we therefore need to deactivate both modules which use this source using `--deactivate-module`
and remove the log source definition from the sigma configuration.

Obviously, this will also impact Aurora's detection capabilities to some degree. Choose your trade-off between detection
and performance carefully.


.. _Process Exclusions:

Process Exclusions
^^^^^^^^^^^^^^^^^^

To exclude specific processes from analysis, you can configure Aurora to ignore all events from specific image paths.

In order to do so, the excluded images must be specified (as regexps) in a file that is passed to ``--process-excludes``.
By default, ``config\process-excludes.cfg`` is used. This file contains further examples on how to specify the
excludes.

The process exclusion file is loaded at startup. If you change the file, you'll need to restart Aurora to apply those changes.

Please be aware that adding process exclusions can cause malware that uses process hollowing or similar techniques to
mask themselves as an excluded process to go unreported.

Examples
~~~~~~~~

.. code::

   # Exclude a specific process
   ^C:\\Program Files\\My Antivirus\\antivirus\.exe$

   # Exclude Windows Defender
   ^C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\[^\\]{5,20}\\MsMpEng\.exe$
