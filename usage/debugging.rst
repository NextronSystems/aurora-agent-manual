Debugging
=========

The best way to debug Aurora is to run it directly in the command line and don't use it as service. 

.. code:: winbatch

    aurora-agent-64.exe --rules-path .\my-rules --debug

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
