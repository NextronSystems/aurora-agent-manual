What is Aurora?
===============

- Aurora is a lightweight endpoint agent that applies Sigma rules and IOCs on local event streams
- It uses Event Tracing for Windows (ETW) to subscribe to certain event channels
- It extends the Sigma standard with so-called "response actions" that trigger after a rule match
- It writes its own events to various outputs: the Windows Eventlog, a log file and remote UDP/TCP targets

What is Aurora Lite? 
====================

Aurora Lite is our free version of Aurora which is free for private and commercial use. The only limitation defined in the TOS is that it cannot be sold or used as part of a paid service. We offer special licensing options for managed detection service providers.

Features and services that are not included in the Aurora Lite version:

- No comfortable Sigma rule management via ASGARD Management Center
- No additional detection modules (non-Sigma-based detection; e.g. Cobalt Strike beaconing, LSASS dumping)
- No private Nextron Sigma rule feed 
- No private Nextron IOC rule feed 
- No encrypted Sigma rules (protect rules from spying eyes or the AV)
- Only 5 rules with response actions allowed

For more details see the description on https://www.nextron-systems.com/aurora
