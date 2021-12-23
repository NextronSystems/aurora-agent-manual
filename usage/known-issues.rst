Known Issues
============

Wrong Image / CommandLine Assignment
----------------------------------

It's possible that under some circumstances the Image field contains a binary that isn't part of the CommandLine field, which is most likely a mapping error. 

Source of Issue
~~~~~~~~~~~~~~~

The reason for this problem is that the information that we use to enrich the original event that only contains a PID and Image doesn't contain a CommandLine field and we use information from a different event channel to add that information. 

Under some circumstances, events can arrive in an order that makes is difficult to assign information from one event to another. 

Affects
~~~~~~~

- Sigma matching in which values of ``CommandLine`` or ``ParentCommandLine`` are used in combination with ``Image`` or ``ParentImage``
- Module: Command Line Mismatch Detector

State 
~~~~~

Work in progress

Missing Self-Defense
--------------------

- Folder permission checks
- ETW manipulations (the ETW canary module already covers some of them)
- Warning events on configuration changes

State
~~~~~

Work in progress
