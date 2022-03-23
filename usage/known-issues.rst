Known Issues
============

x86 Version doesn't start
-------------------------

The ``EtwCanary`` module is broken and doesn't work on x86 systems. You won't get an appropriate error message. The agent just crashes silently on Windows x86 systems. 

Status
~~~~~~

Fixed in build ``4a34c345`` 


Rules that use "Provider_Name" don't match
------------------------------------------

Sigma rules that use the field ``Provider_Name``, e.g. the rule ``Eventlog Cleared`` (UUID: ``d99b79d2-0a6f-4f46-ad8b-260b6e17f982``) that looks for EventID ``1102`` and a certain provider name couldn't match because Aurora uses ``Provider.Name`` internally. 

Status
~~~~~~

Fixed in build ``06b7d44d`` (07.01.2022)

Rule: "Rundll32 Internet Connection" Misses CommandLine Field 
-------------------------------------------------------------

Matches with the rule "Rundll32 Internet Connection" currently miss a ``CommandLine`` field. Adding that field to the rule is already on our list of features. 

Missing Self-Defense
--------------------

- Folder permission checks
- ETW manipulations (the ETW canary module already covers some of them)
- Warning events on configuration changes
