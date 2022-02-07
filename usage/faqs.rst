Frequently Asked Questions
==========================

Why does Aurora generate two alerts for a single event? 
-------------------------------------------------------

Aurora registers to different event channels that sometimes contain the same information. It is possible that Aurora notices the same activity in two different channels and generates two alerts for a single event. 

In these cases, the alerts should have different values set in the ``Provider_Name`` field, e.g. ``Provider_Name: Microsoft-Windows-Kernel-Process`` and ``Provider_Name: Microsoft-Windows-Sysmon``. 

It is difficult to decide which of the two alerts should be suppressed in order to avoid these duplicate notifications.

How do I view the suppressed Sigma matches?
-------------------------------------------

In some messages, e.g. in the reported statistics (``--report-stats``) or the status message (``--status``), you may find a number of suppressed Sigma matches

.. code:: none 

    Event Statistics:
    Events observed so far: 23483429
    Events lost so far: 0
    Sigma matches: 13
    Suppressed Sigma matches of those: 6


Use the flag combination ``--status --trace`` to view which Sigma rule matches have been suppressed. 

.. code:: winbatch 

    C:\Program Files\Aurora Agent\>aurora-agent-64.exe --status --trace
    Aurora Agent
    Version: 0.2.2
    Build Revision: 89227b19
    Signature Revision: 2022/01/27-155103
    Sigma Revision: 0.20-2636-ga8cbfa83
    Status: running
    Uptime (in hours): 0

    Active Outputs:
    Eventlog: enabled
    Stdout: enabled

    Active Modules:
    LsassDumpDetector
    BeaconHunter
    EtwCanary
    CommandLineMismatchDetector
    ProcessTamperingDetector
    TemporaryDriverLoadDetector
    ApplyIOCs

    Rule Statistics:
    Loaded rules: 1186
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 314862
            224706 events from PollHandles
            28606 events from WinEventLog:Microsoft-Windows-Sysmon/Operational
            22538 events from WinEventLog:Microsoft-Antimalware-Engine
            21697 events from WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls
            12018 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_FILEIO?eventids=14
            1620 events from WinEventLog:Microsoft-Windows-PowerShell
            1286 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_IMAGE
            1219 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_THREAD
            539 events from SystemLogger:Process
            257 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_FILENAME
            187 events from WinEventLog:Microsoft-Windows-Kernel-Process/WINEVENT_KEYWORD_PROCESS
            69 events from WinEventLog:Microsoft-Windows-DNS-Client
            31 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_CREATE_NEW_FILE
            26 events from WinEventLog:{fbb4fbaa-2ae9-5b86-6d76-09930a11a03d}?fromownpid=1
            18 events from WinEventLog:Microsoft-Windows-TaskScheduler/Operational
            18 events from WinEventLog:Microsoft-Windows-TCPIP/ut:ConnectPath
            11 events from WinEventLog:Security
            9 events from WinEventLog:Microsoft-Windows-WinINet/WININET_KEYWORD_HANDLES
            7 events from WinEventLog:Microsoft-Windows-Kernel-File/KERNEL_FILE_KEYWORD_DELETE_PATH
    Events lost so far: 0
    Sigma matches: 13
            LSASS Memory Dump: 13
    Suppressed Sigma matches of those: 6
            LSASS Memory Dump: 6

    Response Actions: disabled

The match throttling can be configured with the flags ``--match-burst`` and ``--match-throttling``. We recommend keeping it in the default. It does not suppress  matches of a certain rule that you haven't already noticed in the defined time frame. It throttles numerous matches of a single rule; cases in which a single rule causes numerous matches in the defined time frame, which is typically the cause of a noisy / too sensitive rule. 
