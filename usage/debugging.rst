Debugging
=========

The best way to debug Aurora is to run it directly in the command line and don't use it as service. 

.. code-block:: doscon

    C:\Program Files\Aurora Agent\>aurora-agent-64.exe --rules-path .\my-rules --debug

The verbosity can even be increased by using the ``--trace`` flag. With ``--trace``,
a log entry will be generated for every incoming event.

``--debug`` and ``--trace`` apply to all outputs (log file, UDP / TCP, command line) except for the Windows Eventlog,

Status Information
------------------

The ``--status`` can give you information from a running Aurora service.

.. literalinclude:: ../examples/status
   :language: doscon
   :linenos:

It displays the number of events that the agent was able to see and process, the number of initialized rules and rule matches. 

Adding the flag ``--trace`` includes more information in the output, e.g. the number of processed events per ETW event channel.

.. literalinclude:: ../examples/status-trace
   :language: doscon
   :linenos:

The JSON output includes all the information plus the agent configuration settings. 

.. literalinclude:: ../examples/status-json
   :language: doscon
   :linenos:

Diagnostic information
----------------------

Diagnostic pack
^^^^^^^^^^^^^^^

You can create a diagnostic pack to detect and debug performance problems.

Simply run:

.. code-block:: doscon 

    C:\Program Files\Aurora Agent>aurora-agent-util.exe diagnostics

This creates a ZIP file with debugging information (such as heap usage, stack traces, ...)
that we can use to analyze these issues.

Profiling server
^^^^^^^^^^^^^^^^

If Aurora has been started with ``--pprof``, information can also be gathered manually via a web interface: 

.. code-block:: batch 

    curl.exe http://localhost:8080/debug/pprof/profile?seconds=20 --output aurora-debug.pprof
    curl.exe http://localhost:8080/debug/pprof/heap --output aurora-heap.pprof
    curl.exe http://localhost:8080/debug/pprof/goroutine --output aurora-stack-traces.pprof

This is the same information that is included in the diagnostic pack.

Crashes 
-------

In cases of unexpected crashes, the following command lines can help you identify the source of the problem. 

.. code-block:: doscon 

    C:\Program Files\Aurora Agent>aurora-agent.exe -c agent-config.yml > aurora-crash.log 2>&1

.. code-block:: doscon 

    C:\Program Files\Aurora Agent>aurora-agent.exe -c agent-config.yml --trace > aurora-crash-trace.log 2>&1

Error Messages
--------------

Check the configured log outputs for error messages. A faulty rule would e.g.
lead to error messages like this one in the ``Application`` eventlog with EventID 

.. code-block:: none

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

.. code-block:: none

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

.. code-block:: none

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

.. code-block:: yaml

   windows-api-call-auditing:
      product: windows
      service: api-call-auditing
      sources:
         - "WinEventLog:Microsoft-Windows-Kernel-Audit-API-Calls"

To deactivate this log source, we therefore need to deactivate both modules which use this source using `--deactivate-module`
and remove the log source definition from the sigma configuration.

Obviously, this will also impact Aurora's detection capabilities to some degree. Choose your trade-off between detection
and performance carefully.

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

.. code-block::

   # Exclude a specific process
   ^C:\\Program Files\\My Antivirus\\antivirus\.exe$

   # Exclude Windows Defender
   ^C:\\ProgramData\\Microsoft\\Windows Defender\\Platform\\[^\\]{5,20}\\MsMpEng\.exe$
