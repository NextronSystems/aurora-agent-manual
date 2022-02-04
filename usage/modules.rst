Modules
=======

This chapter lists all detection and self-protection modules included in the full version of Aurora.

Cobalt Strike Beacon Hunter
---------------------------

Detects suspicious processes beaconing to remote systems based on certain communication patterns often found in C2 frameworks, especially Cobalt Strike. 

LSASS Dump Detector
-------------------

Generic detection of LSASS process dumping.

ETW Canary 
----------

A detector module that tries to detect tampering with the ETW channels. (self-defence mechanism)

Command Line Mismatch Detector 
------------------------------

Detects `process ghosting <https://pentestlaboratories.com/2021/12/08/process-ghosting/>`_ and similar process creation anomalies. 

Process Tampering Detector
--------------------------

Detects privilege escalation to LOCAL_SYSTEM within a process context and PPL protection changes (e.g. MimiDrv process manipulation)

Temporary Driver Load Detector
------------------------------

Detects driver loading events in which a driver is loaded and quickly unloaded afterwards, which could be a sign of malicious activity.