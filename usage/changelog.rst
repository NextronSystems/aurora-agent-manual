Changelog
=========

This chapter contains all new changes of Aurora.

Aurora Agent 1.2
################

Aurora Agent Version 1.2.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added sigma tags to output when printing Sigma matches

Aurora Agent Version 1.2.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where the integrity levle of user processes was not correctly determined
    * - Bugfix
      - Fixed a bug where process starts were seen as remote thread creations

Aurora Agent Version 1.2.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where remote thread creation events were not recognized correctly

Aurora Agent Version 1.2.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where too many filename IOCs could cause initialization to fail
    * - Update
      - YARA to v4.5.1
    * - Update
      - Golang to 1.20.13

Aurora Agent Version 1.2.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where NT paths starting with ``\Windows\`` were not correctly converted to DOS paths

Aurora Agent Version 1.2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added temporary excludes for process / provider / event ID combinations with very high event rates
    * - Feature
      - Improved speed of sigma rule matching
    * - Feature
      - Added support for polling log files
    * - Feature
      - Removed support for custom actions
    * - Bugfix
      - Fixed an issue where Aurora could crash if too many handles were open
    * - Feature
      - Added Trace Event Tab in Dashboard

Aurora Agent 1.1
################

Aurora Agent Version 1.1.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where the handle polling provider did not handle large PIDs correctly

Aurora Agent Version 1.1.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where some new log sources were not loaded properly

Aurora Agent Version 1.1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where small files could cause issues with magic header detection

Aurora Agent Version 1.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue where Aurora could leak process handles when analyzing stack traces, possibly leading to high memory load when running for a long time
    * - Feature
      - Added functionality to the ResControl module to terminate Aurora if a handle leak is detected

Aurora Agent Version 1.1.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added a field for process creation events that indicates whether process parent spoofing took place
    * - Feature
      - Added support for call traces from ETW events. Extended call traces (with full symbols) are also possible.
    * - Feature
      - Added CallTrace (and, in intense configuration, CallTraceExtended) fields to OpenProcess events
    * - Feature
      - Added new flags to set output format specifically for some outputs
    * - Feature
      - Added a ``--dashboard`` option that starts an interactive notifier for checking recent Aurora events
    * - Bugfix
      - Fixed an issue where rules with multiple wildcards could cause extremely high memory usage

Aurora Agent 1.0
################

Aurora Agent Version 1.0.7
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed an issue in go-sigma that can lead to high memory usage during initialization
    * - Feature
      - Added default exclusion for Windows Defender

Aurora Agent Version 1.0.6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Improved performance of Sigma rule matching
    * - Feature
      - Added a new log source for 'NtSetInformationKey' calls
    * - Feature
      - Added a timeout for receiving the agent status

Aurora Agent Version 1.0.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Removed unnecessary files from ZIP package
    * - Bugfix
      - Fixed an issue where memory was leaked over time

Aurora Agent Version 1.0.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved logging of file hash calculation

Aurora Agent Version 1.0.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved handling of signals received during Aurora startup

Aurora Agent Version 1.0.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Made additional flags available from ASGARD
    * - Feature
      - Added a warning when using keyword IOCs

Aurora Agent Version 1.0.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where an invalid rule caused the full ruleset to not be loaded

Aurora Agent Version 1.0.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where diagnostics pack creation could hang
    * - Feature
      - Added specific 'registry_*' categories in log source mappings

Aurora Agent 0.9
################

Aurora Agent Version 0.9.9
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Extended 'diagnostics' information to cover broken configurations better
    * - Feature
      - Incorrect flags used in configuration file now cause Aurora startup to fail

Aurora Agent Version 0.9.8
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Upgraded to Golang 1.17
    * - Feature
      - Added a new 'diagnostics' command to Aurora Util that extracts information useful for debugging

Aurora Agent Version 0.9.7
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where registry events weren't applied correctly
    * - Bugfix
      - Fixed a bug where the TemporaryDriverLoadDetector did not contain useful information

Aurora Agent Version 0.9.6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved formatting of events displayed by '--trace'
    * - Change
      - Improved handling of custom responses with nonexistent fields
    * - Change
      - Improved handling of invalid log source files

Aurora Agent Version 0.9.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added explicit information about enabled modules to '--module-info'

Aurora Agent Version 0.9.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where backslashes in custom responses were parsed incorrectly
    * - Bugfix
      - Fixed a bug where events that indirectly originated from Aurora (e.g. via Sysmon) were processed
    * - Bugfix
      - Fixed a bug where some response events had an incorrect log ID
    * - Feature
      - Added IOC counts to status
    * - Bugfix
      - Fixed a bug where explorer.exe could be terminated even if 'lowprivonly' was set

Aurora Agent Version 0.9.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Decreased time needed to stop Aurora
    * - Bugfix
      - Fixed a bug where certain responses could lead to a deadlock in response execution
    * - Bugfix
      - Fixed a bug where the log file was not recreated when it was deleted
    * - Bugfix
      - Fixed a bug where '--restart-service' did not work as intended
    * - Bugfix
      - Fixed a bug where faulty hash IOCs were silently ignored

Aurora Agent Version 0.9.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - TCP log target now tries to reconnect if the connection is interrupted
    * - Feature
      - Aurora Agent Util's 'upgrade' now also upgrades the installed agent when run with '--restart-service'

Aurora Agent Version 0.9.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Renamed providers to have similar naming patterns for all modules
    * - Change
      - Changed indentation for '--status'
    * - Bugfix
      - Fixed a bug where ProcessTree contained incorrect elements

Aurora Agent Version 0.9.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Improved performance for many matching operations

Aurora Agent 0.8
################

Aurora Agent Version 0.8.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug regarding decision making whether a process is considered high privileged

Aurora Agent Version 0.8.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Clarified log messages if responses are simulated
    * - Change
      - Clarified log messages for IOC matches

Aurora Agent Version 0.8.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Renamed the 'FileAge' field to 'ImageAge' for many events
    * - Feature
      - Improved debug logging
    * - Feature
      - Added 'ParentCommandLine' field to some file events
    * - Feature
      - Added information about grandparent process to process creation events
    * - Feature
      - Added 'ProcessTree' field to process creation events

Aurora Agent Version 0.8.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - The default locations for process exclude and false positive exclusion files have been moved to the new 'config/' directory
    * - Change
      - The number of process excludes and false positive exclusions is now part of the agent status
    * - Feature
      - Added 'exclude' command to Aurora Agent Util for a dialogue to exclude processes causing many events

Aurora Agent 0.7
################

Aurora Agent Version 0.7.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--process-exclude' parameter that can be used to filter out events from specific processes early
    * - Bugfix
      - Fixed a bug that could potentially lead to deadlocks
    * - Feature
      - Added ResControl module to terminate Aurora if memory usage is too excessive
    * - Feature
      - Added information about events received per process to '--status --trace' output

Aurora Agent 0.6
################

Aurora Agent Version 0.6.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where some content information was missing from events

Aurora Agent Version 0.6.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved output for response execution

Aurora Agent Version 0.6.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Deprecated 'killparent' which was replaced by 'processidfield'
    * - Feature
      - Added lookup of parent process using cached data for responses
    * - Feature
      - Added 'emp' response action

Aurora Agent Version 0.6.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added 'processidfield' flag for responses using 'kill', 'suspend' or 'dump'
    * - Change
      - Change '--deactivate-all-modules' to '--deactivate-all-consumers'
    * - Feature
      - Added support for 'response: none' to explicitly overwrite a response with one that does nothing

Aurora Agent Version 0.6.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--response-set' flag for external definitions of responses for sigma rules
    * - Bugfix
      - Fixed a bug where some events did not contain the process ID as expected by responses
    * - Feature
      - Added 'all' as a valid value for the 'ancestors' flag

Aurora Agent 0.5
################

Aurora Agent Version 0.5.8
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Added descriptions for all modules

Aurora Agent Version 0.5.7
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added additional information for ASGARD's parameter representation
    * - Change
      - Unified module list for Windows and Linux builds
    * - Change
      - Included providers in '--module-list'

Aurora Agent Version 0.5.6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Allowed deactivation of providers
    * - Bugfix
      - Fixed an issue where some sigma rule matches were reported as Info level instead of Notice

Aurora Agent Version 0.5.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--quiet' flag for ASGARD
    * - Feature
      - Added more log IDs for identification
    * - Bugfix
      - Fixed a bug where '--restart-service' would fail if the Aurora service was stopped

Aurora Agent Version 0.5.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved identification of processes for correlation purposes

Aurora Agent Version 0.5.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Improved handling of allocations, reduced temporary allocations during event analysis

Aurora Agent Version 0.5.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added exclusions to intrusive tampering detectors
    * - Feature
      - '--json' now also applies to eventlog output
    * - Bugfix
      - Fixed a bug where Aurora Agent Util downloaded upgrades / updates even when not necessary

Aurora Agent Version 0.5.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added log source for 'WinEventLog:Microsoft-Windows-Windows Firewall With Advanced Security/Firewall'
    * - Change
      - Removed unnecessary completion command in Aurora Agent Util

Aurora Agent Version 0.5.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added detection for 'EtwEventWrite' patches to process tampering detector
    * - Bugfix
      - Fixed a bug where hash order was not constant

Aurora Agent 0.4
################

Aurora Agent Version 0.4.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Changed the scheduled task names to be better understandable
    * - Feature
      - Added an additional log source for virtual disk mounts
    * - Change
      - Administrator tokens now count as low privileged for 'lowprivonly' (only LOCAL SYSTEM and similar tokens are protected)

Aurora Agent Version 0.4.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where installation paniced in certain race conditions
    * - Feature
      - Added better support for file names in events from 'Microsoft-Windows-Kernel-File'

Aurora Agent Version 0.4.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added 'Alert' and 'Notice' log levels to better distinguish internal error / info messages and matches
    * - Bugfix
      - Fixed a bug where a handle was not correctly closed
    * - Change
      - Improved error message when receiving a Sigma correlation rule
    * - Change
      - Improved output when failing to parse the command line

Aurora Agent Version 0.4.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where Aurora installation timed out
    * - Change
      - Improved output if Aurora service failed to start after installation
    * - Bugfix
      - Fixed a bug where '--uninstall' failed when run from the installed Aurora executable
    * - Bugfix
      - Fixed a bug where a segmentation fault in the eventlog API was visible to the user

Aurora Agent Version 0.4.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Startup errors when running as a service are now written to 'service-startup.log' next to the executable
    * - Change
      - There are now two scheduled tasks: one for upgrades, one for updates
    * - Feature
      - Added '--report-stats-verbose' flag for more information in '--report-stats' output
    * - Bugfix
      - Fixed a bug where signatures where updated even when this was unnecessary
    * - Change
      - Installation now adds the installation path to the PATH environment variable

Aurora Agent 0.3
################

Aurora Agent Version 0.3.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug where Aurora indefinitely tried to restart after a startup error
    * - Bugfix
      - Fixed a bug where the installed service still referred to the paths as they were prior to installation
    * - Bugfix
      - Fixed a bug where Aurora didn't update the signatures daily
    * - Change
      - Updated description for many flags in '--help'
    * - Change
      - Process dumps are now written to the 'process-dumps' folder by default instead of the working directory
    * - Feature
      - Added banner display for interactive runs
    * - Feature
      - Added a default file for '--false-positive-filter' that includes a usage example
    * - Feature
      - Added rule paths to '--status' output
    * - Change
      - Specifying positional arguments (which were ignored before) now causes an error

Aurora Agent 0.2
################

Aurora Agent Version 0.2.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added support for DestinationIsIpv6 in Microsoft-Windows-TCPIP events
    * - Change
      - Improved installation procedure to account for user interrupts
    * - Feature
      - Added custom-signatures folder that is on the search list by default
    * - Change
      - Improved handling of panics and runtime faults

Aurora Agent Version 0.2.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Active and Inactive modules are listed at startup
    * - Feature
      - Added more verbose output to installation success

Aurora Agent Version 0.2.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Signature revision is now included in status and initial message
    * - Change
      - Events from the named pipe poller now include the process that has a handle to the named pipe
    * - Change
      - The named pipe polling provider now provides polling for all handles on the system
    * - Change
      - Command lines from existing processes at Aurora startup are now properly cached

Aurora Agent Version 0.2.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed bug that caused the version numbers to be empty in Eventlog
    * - Bugfix
      - Fixed overlaps with Event IDs of different modules (default ID 199)
    * - Change
      - Lowered score of driver loads from System32 folder (TemporaryDriverLoadDetector)

Aurora Agent Version 0.2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Disabled EtwCanary for x86 systems due to issues with Windows 10 x86
    * - Bugfix
      - Fixed a bug where the prodcess tampering detector caused panics on Windows 7
    * - Change
      - Errors in single sigma rules no longer cause the Aurora Agent startup to fail
    * - Feature
      - Added '--false-positive-filter-file' for custom exclusions
    * - Change
      - Aurora now installs all files to C:\Program Files\Aurora Agent and none to C:\ProgramData
    * - Feature
      - Added '--force' flag to Aurora Agent Util for forced upgrades
    * - Feature
      - Aurora Agent Util is now installed and can be used to update the installed version directly
    * - Feature
      - Aurora Agent now adds a daily update scheduled tasks on installation

Aurora Agent 0.1
################

Aurora Agent Version 0.1.12
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Bugfix
      - Fixed a bug in Sigma matching that could cause false negatives
    * - Change
      - Unified startup log lines into a single message
    * - Feature
      - Added module for process tampering detection
    * - Feature
      - Added module for temporary driver detection
    * - Feature
      - Added '--deactivate-all-modules' for easier debugging
    * - Feature
      - Added '--sigdev' option for Aurora Agent Util
    * - Feature
      - Added module for IOC (filenames, domains, hashes, ... ) application
    * - Change
      - Renamed '--no-content-info' to '--no-content-enrichment'

Aurora Agent Version 0.1.11
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added an ETW Canary module that checks whether ETW events are received
    * - Feature
      - Added content information via correlation to many events
    * - Change
      - Restricted number of active responses to 2 for Aurora Agent Lite
    * - Feature
      - Added FileAge field for content information
    * - Feature
      - Added Aurora Signature pack, Aurora Signatures can be updated with Aurora Util

Aurora Agent Version 0.1.10
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added a whitelist as beaconhunter excludes
    * - Bugfix
      - Fixed a bug where the UDP socket permanently broke down
    * - Feature
      - Added more context information to beaconhunter messages
    * - Change
      - Sigma can now be deactivated with '--deactivate-module Sigma'
    * - Change
      - BeaconHunter no longer activates expensive event sources by default, but still uses them if others activate them
    * - Change
      - Renamed '--no-hashes' to the more accurate '--no-content-info'

Aurora Agent Version 0.1.9
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added log id for status messages
    * - Bugfix
      - Fixed a FP in LSASS dump check
    * - Feature
      - Added more information for TCP connections

Aurora Agent Version 0.1.8
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Moved log source mappings to a separate file that is shared for all configurations
    * - Bugfix
      - Fixed a bug where process information could be misinterpreted when a process ID was reused
    * - Feature
      - Added more content information for PE files (version resource information)

Aurora Agent Version 0.1.7
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added registry kernel logger as default source, values and paths are now parsed correctly
    * - Bugfix
      - Fixed a bug where process information was discarded too early
    * - Bugfix
      - Fixed a bug where Aurora didn't register properly for kernel providers if it was terminated harshly

Aurora Agent Version 0.1.6
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--print-event-id' option
    * - Bugfix
      - Fixed a bug where errors in other ETW sessions could affect Aurora

Aurora Agent Version 0.1.5
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--no-hashes' option
    * - Bugfix
      - Fixed a race condition where log sources were not updated properly on sigma log source change
    * - Bugfix
      - Fixed a bug where hash calculation didn't close its file mapping properly
    * - Change
      - Log sources are now in a separate folder
    * - Feature
      - Added four agent configurations (minimal, reduced, standard, intense) for common use cases
    * - Change
      - Renamed 'sigma-config' to '--log-source'
    * - Bugfix
      - Fixed a bug where debugging output from the imphash calculation was visible
    * - Change
      - Disabled quick edit mode in a console while Aurora is running

Aurora Agent Version 0.1.4
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added MD5, SHA1, SHA256 hashes as well as imphashes to process creation, image load, and driver load events
    * - Feature
      - Added Aurora Util for Aurora upgrades and rule encryption
    * - Feature
      - Added example for proper named pipe detection using SystemLogger:Handle
    * - Change
      - Expanded Log IDs, defined different Log ID ranges for the different modules

Aurora Agent Version 0.1.3
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Change
      - Renamed '--event-throttling' to '--output-throttling', it now drops events instead of slowing Aurora
    * - Bugfix
      - Fixed a bug where the log file wasn't written after installation
    * - Feature
      - Added '--low-prio' for reduced process priority, changed default priority to normal
    * - Change
      - Added '--sigma-match-throttling' and '--sigma-match-burst' for limiting sigma matches on a per-rule basis
    * - Change
      - aurora-agent now calls aurora-agent-64 when called on a 64 bit platform
    * - Feature
      - Added missing log source rewrite for systemlogger-process
    * - Change
      - Grouped "source not found" messages
    * - Change
      - Rules may now define multiple responses
    * - Change
      - Event Log IDs are now equal to Sysmon Event IDs for common sigma categories
    * - Change
      - Custom fields are now marshaled to YAML in string form
    * - Change
      - CPU limit now measures only CPU usage of Aurora

Aurora Agent Version 0.1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added '--event-throttling' option for slowed output
    * - Feature
      - Added '--no-stdout' option for no logging to stdout
    * - Feature
      - Added '--module-info' option to enumerate existing modules
    * - Bugfix
      - Fixed a bug where some parameters weren't written to the installed config
    * - Change
      - Expanded '--status' output
    * - Feature
      - Added support for response options: recursive, ancestors, and simulate
    * - Feature
      - Added output for simulated responses
    * - Bugfix
      - Fixed a bug where Aurora could match events that it wrote itself
    * - Bugfix
      - Fixed a bug where fields available for sigma matching and responses were inconsistent
    * - Feature
      - Added Aurora Agent Icon

Aurora Agent Version 0.1.1
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Feature
      - Added support for activating and deactivating single consumers
    * - Change
      - Allowed query syntax with ETW channels to request only specific event IDs
    * - Feature
      - Added build revision support

Aurora Agent Version 0.1.0
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
    :header-rows: 1
    :widths: 15, 85

    * - Type
      - Description
    * - Major Release
      - Initial Release