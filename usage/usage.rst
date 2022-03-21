Usage
=====

This chapter explains some more frequently used command line options used by Aurora in more detail.

Run Aurora
----------

If you simply run Aurora in your terminal, it'll use the default values for each flag and no dedicated config file:

.. code:: winbatch
    
    aurora-agent-64.exe

You can select one of the default config presets with the respective flag:

.. code:: winbatch
    
    aurora-agent-64.exe -c agent-config-reduced.yml

A typical command line that runs Aurora and prints messages and matches to the command line and the Windows ``Application`` eventlog looks like this:

.. code:: winbatch 

    aurora-agent-64.exe --minimum-level low

Run Aurora as Service
---------------------

To install Aurora as a service, use the ``--install`` flag and see the chapter :doc:`installation </usage/installation>` for more details.

A typical installation on systems that have limited hardware resources could look like this. 

.. code:: winbatch
    
    aurora-agent-64.exe --install -c agent-config-reduced.yml

We ship Aurora with 4 presets that we recommend to use. See the chapter :doc:`configuration </usage/configuration>` for more information.

Status Information
------------------

This flag can be used to query status information from the running service.

Note: Make sure to also set ``--agent-name`` if you've set a non-standard name.

This flag can be combined with the ``--json`` and ``--trace`` flags for JSON formatted or more detailed output.

.. code:: none

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
                "C:\\Program Files\\Aurora-Agent\\rules",
                "C:\\Program Files\\Aurora-Agent\\myrules"
            ],
            "AutoReload": false,
            "LogFile": "",
            "LogSources": [
                "C:\\Program Files\\Aurora-Agent\\default-log-sources.yml",
                "C:\\Program Files\\Aurora-Agent\\etw-log-sources.yml"
            ],
            "Debug": false,
            "Trace": false,
            "EventLogging": true,
            "ReportingLevel": "high",
            "DumpFolder": "C:\\Program Files\\Aurora-Agent\\process-dumps",
            "Json": false,
            "LicensePath": "C:\\Program Files\\Aurora-Agent\\aurora",
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

You can combine the ``--status`` flag with the ``--trace`` flag to get a more detailed version. 

.. code:: 

    Aurora Agent
    Version: 0.1.4
    Build Revision: d79fa653
    Sigma Revision: 0.20-1706-g653950e4
    Status: running
    Uptime (in hours): 0

    Active Outputs:
    Eventlog: enabled
    Stdout: enabled

    Rule Statistics:
    Loaded rules: 1030
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 85605
            42177 events from WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
            20095 events from WinEventLog:Microsoft-Windows-Sysmon/Operational
            19164 events from WinEventLog:Microsoft-Antimalware-Engine
            2356 events from PollNamedPipes
            857 events from WinEventLog:Microsoft-Windows-Kernel-Registry/CreateKey
            527 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_IMAGE
            157 events from SystemLogger:Process
            126 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_PROCESS
            31 events from WinEventLog:Microsoft-Windows-TaskScheduler/Operational
            29 events from WinEventLog:Microsoft-Windows-DNS-Client
            25 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_CREATE_NEW_FILE
            25 events from WinEventLog:Microsoft-Windows-TCPIP/ut:ConnectPath
            19 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_DELETE_PATH
            12 events from WinEventLog:Security
            4 events from WinEventLog:Microsoft-Windows-Kernel-Registry/DeleteKey
            1 events from WinEventLog:Application
    Events lost so far: 0
    Sigma matches: 91
            New TaskCache Entry: 18
            Suspicious In-Memory Module Execution: 4
            Credentials Dumping Tools Accessing LSASS Memory: 69
    Suppressed Sigma matches of those: 74
            New TaskCache Entry: 12
            Credentials Dumping Tools Accessing LSASS Memory: 62

    Response Actions: disabled

Tracing Events
--------------

Using the ``--trace`` flag you can view all the events Aurora observes in the different subscribed channels. 

It's a good idea to write the output to a file in order to search in it later. 

.. code:: winbatch

    aurora-agent-64.exe --trace > d:\aurora-trace.log
