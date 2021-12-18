Configuration
=============

Aurora uses the YAML format for its configuration file. All values set in the config file can also be used as command line flags. 

Since there are two modes of operation 

1. Aurora started from command line using a config passed with the ``--config`` / ``-c`` flag
2. Aurora started as a service with a config file located in ``C:\Program Files\Aurora-Agent\agent-config.yml`` (see chapter :doc:`installation </usage/installation>` for more details)

Configuration Profiles
----------------------

To facilitate the use of Aurora, we provide 

1. Minimal 
2. Reduced
3. Standard
4. Intense 

Minimal 
~~~~~~~

Inactive ETW Sources 

- Registry
- Image Loads 
- Raw Disk Access
- Process Access
- Create Remote Thread

Agent Config 

TBD

Reduced 
~~~~~~~

Inactive ETW Sources 

- Registry
- Raw Disk Access
- Process Access

Standard
~~~~~~~~

Inactive ETW Sources 

- Registry
- Raw Disk Access

Intense 
~~~~~~~

All possible ETW log source are activated. 

WARNING: This preset uses the most system resources and can put the system under heavy load, especially if a process accesses many registry keys in a short amount of time. 

We recommend using this preset only on a very selective set of systems or in cases in which maximum detection is required. 

Examples 
--------

A default configuration file looks like this:

.. code:: yaml
    
    # Paths containing the sigma files
    rules-path:
        - .\rules
    # Automatically reload the sigma rules and configurations upon detecting changes
    auto-reload: false
    # Log file path
    logfile: ''
    # Paths to the sigma configurations that should be loaded
    sigma-config:
        - .\default-log-sources.yml
        - .\etw-log-sources.yml
    # Print debugging information
    debug: false
    # Print tracing information
    trace: false
    # Don't log matches to the Windows event log
    no-eventlog: false
    # Report Sigma matches with rules of this level or higher
    minimum-level: high
    # Write output as JSON instead of plain text
    json: false
    # Path to the directory containing the Aurora Agent license
    license-path: .
    # UDP Address (as host:port) where the Aurora Agent should write its logs to
    udp-target: ''
    # Don't print any logs
    silent: false
    # Percentage of a single CPU core that the Aurora Agent should use at most
    cpu-limit: 100
    # Log a message about the current agent status regularly
    report-stats: false
    # Interval between status messages, see --report-stats
    report-stats-interval: 1h
    # How many log rotations should be retained
    log-rotate: 7
    # At which size the log should be rotated
    log-size: 10MB
    # Set a different name for the service, the binary and other identifiers
    agent-name: aurora-agent
    # Activate the given modules, even if they are disabled by default
    activate-module: []
    # Deactivate the given modules
    deactivate-module: []
    # Disable logging to the standard output
    no-stdout: false
    # minimum average time between log messages (warning: if set, it will slow down Aurora Agent if many matches occur!)
    event-throttling: 0h
    # Execute responses that are specified in sigma rules (e.g. to kill a process)
    activate-responses: false
    # Folder where process dumps should be stored
    dump-folder: .

A typical configuration file would look like this 

.. code:: yaml

    # Paths containing the sigma files
    rules-path:
        - C:\ProgramData\Aurora-Agent\rules
    # Automatically reload the sigma rules and configurations upon detecting changes
    auto-reload: false
    # Log file path
    logfile: ''
    # Paths to the sigma configurations that should be loaded
    sigma-config:
        - C:\Program Files\Aurora-Agent\default-log-sources.yml
        - C:\Program Files\Aurora-Agent\etw-log-sources.yml
    # Print debugging information
    debug: false
    # Print tracing information
    trace: false
    # Don't log matches to the Windows event log
    no-eventlog: false
    # Report Sigma matches with rules of this level or higher
    minimum-level: high
    # Write output as JSON instead of plain text
    json: false
    # Path to the directory containing the Aurora Agent license
    license-path: C:\ProgramData\Aurora-Agent\Aurora
    # UDP Address (as host:port) where the Aurora Agent should write its logs to
    udp-target: ''
    # Don't print any logs
    silent: false
    # Percentage of a single CPU core that the Aurora Agent should use at most
    cpu-limit: 100
    # Log a message about the current agent status regularly
    report-stats: false
    # Interval between status messages, see --report-stats
    report-stats-interval: 1h
    # How many log rotations should be retained
    log-rotate: 7
    # At which size the log should be rotated
    log-size: 10MB
    # Set a different name for the service, the binary and other identifiers
    agent-name: aurora-agent
    # Activate the given modules, even if they are disabled by default
    activate-module: []
    # Deactivate the given modules
    deactivate-module: []
    # Disable logging to the standard output
    no-stdout: false
    # minimum average time between log messages (warning: if set, it will slow down Aurora Agent if many matches occur!)
    event-throttling: 0h
    # Execute responses that are specified in sigma rules (e.g. to kill a process)
    activate-responses: false
    # Folder where process dumps should be stored
    dump-folder: C:\ProgramData\Aurora-Agent\process-dumps

Output Options
--------------

The following output options are currently available 

- Windows Eventlog (default)
- Log file
- UDP target (full version only)
- ASGARD Analysis Cockpit (full version only)
- Standard Output

ASGARD Analysis Cockpit 
~~~~~~~~~~~~~~~~~~~~~~~

Whenever you install an ASGARD Agent, the controlled Aurora Agent Services gets its configuration automatically. In a default setup, all logs generated by an Aurora Agent will be relayed via an ASGARD to an Analysis Cockpit system.

Standard Output
~~~~~~~~~~~~~~~

The standard output can be used for debugging purposes. It contains all the matching events plus debugging and tracing messages when set to ``True`` in the config file. 
