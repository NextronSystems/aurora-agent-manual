What is Aurora?
===============

- Aurora is a lightweight endpoint agent that applies Sigma rules on local event streams.
- It uses Event Tracing for Windows (ETW) to subscribe to certain event channels.
- It extends the Sigma standard with so-called "response actions" that can get executed after a rule match
- It supports multiple output channels: the Windows Eventlog, a log file and remote UDP targets
- 

What is Aurora Lite? 
--------------------

Aurora Lite is our free version of Aurora. It has a few limitations, doesn't use our private Sigma rule set, lacks comfort features and special modules. 

Additional features in the full version:

- Comfortable Aurora Agent and Sigma rule management via ASGARD Management Center
- Additional detection modules (not Sigma-based; e.g. Cobalt Strike beaconing, LSASS dumping)
- Nextron Sigma rule feed 
- Encrypted Sigma rules (protect rules from spying eyes or the AV)
