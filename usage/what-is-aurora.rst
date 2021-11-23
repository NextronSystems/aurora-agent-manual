What is Aurora?
===============

- Aurora is a lightweight endpoint agent that applies Sigma rules on local event streams.
- It uses Event Tracing for Windows (ETW) to subscribe to certain event channels.
- It extends the Sigma standard with so-called "response actions" that can get executed after a rule match
- It supports multiple output channels: the Windows Eventlog, a log file and remote UDP targets
- 

What is Aurora Lite? 
--------------------

Aurora Lite is our free version of Aurora which is free for private and commercial use. The only limitation in the TOS is that it cannot be sold or used as part of a paid service. We offer special licensing options for managed detection and response service providers.

It has a few technical limitations, doesn't use our private Sigma rule set, lacks resource control features and special modules. 

Additional features in the full version:

- Comfortable Aurora Agent and Sigma rule management via ASGARD Management Center
- Additional detection modules (not Sigma-based; e.g. Cobalt Strike beaconing, LSASS dumping)
- Nextron Sigma rule feed 
- Encrypted Sigma rules (protect rules from spying eyes or the AV)
- Log output rate throttling 
- CPU load limiting
