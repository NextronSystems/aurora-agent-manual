Modules
=======


This chapter lists all modules included in the full version of Aurora.

Providers
---------

Providers are modules that do not detect anything on their own. Instead,
they provide events to consumers. Each consumer requests a list of
`log sources`, which are passed to the providers. The providers then
send the events from that log source to the consumers that
requested it.

ETW Source
~~~~~~~~~~

Starts an ETW session and registers for ETW providers to receive events from them.

ETW Kernel Source
~~~~~~~~~~~~~~~~~

Starts a SystemTraceProvider ETW session (see
`Microsoft's Documentation <https://docs.microsoft.com/en-us/windows/win32/etw/configuring-and-starting-a-systemtraceprovider-session>`_)
and registers for System Providers to receive events from them.

Eventlog Source
~~~~~~~~~~~~~~~

Regularly polls event logs for new events.

Poll Handles
~~~~~~~~~~~~

Regularly polls all handles on a system.

Consumers
---------

Consumers contain detection and self-protection logic. They register for
specific `log sources` that they require in order to work.

Cobalt Strike Beacon Hunter
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detects suspicious processes beaconing to remote systems based on certain
communication patterns often found in C2 frameworks, especially Cobalt Strike. 

LSASS Dump Detector
~~~~~~~~~~~~~~~~~~~

Generic detection of LSASS process dumping.

ETW Canary 
~~~~~~~~~~

A detector module that tries to detect tampering with the ETW channels. (self defense mechanism)

Command Line Mismatch Detector 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detects `process ghosting <https://pentestlaboratories.com/2021/12/08/process~ghosting/>`_
and similar process creation anomalies. 

Process Tampering Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~

Detects privilege escalation to LOCAL_SYSTEM within a process context and PPL protection
changes (e.g. MimiDrv process manipulation)

Temporary Driver Load Detector
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detects driver loading events in which a driver is loaded and quickly unloaded afterwards,
which could be a sign of malicious activity.