Performance Tuning
==================

Event Source Tuning
-------------------

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

  Channel and options are optional and add further restrictions on events from the channel that are
  requested.
  A full list of Eventlog channels on a system can be found using the Event Viewer. A full list of ETW providers on a system
  can be found using e.g. https://github.com/zodiacon/EtwExplorer.
- ``SystemLogger:`` Events from the System Trace Provider
  (see https://docs.microsoft.com/en-us/windows/win32/etw/configuring-and-starting-a-systemtraceprovider-session for details).

  The schema is: ``SystemLogger:SystemLoggerFlag`` and the supported flags are:

  - FileIO
  - Process
  - Thread
  - Registry
  - Image
  - Network-TCP-IP
  - Handle
- ``PollHandles``: This event source is handled by a provider in Aurora that regularly creates an event for each handle that exists on a system.

Example: Disabling a noisy log source
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

Process exclusions
------------------

To exclude specific processes from analysis, you can configure Aurora to ignore all events from specific image paths.

In order to do so, the excluded images must be specified (as regexps) in a file that is passed to ``--process-excludes``.
By default, ``custom-signatures/process-excludes.txt`` is used. This file contains further examples on how to specify the
excludes.

Please be aware that adding process exclusions can cause malware that uses process hollowing or similar techniques to
mask themselves as an excluded process to go unreported.

Examples
~~~~~~~~

.. code::

   # Exclude a specific process
   ^C:\\Program Files\\My Antivirus\\antivirus\.exe$

   # Exclude a directory
   ^C:\\Program Files\\Some Folder\\