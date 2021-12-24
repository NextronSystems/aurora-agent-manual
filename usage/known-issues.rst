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

Status
~~~~~~

Work in progress. Fix in January.

x86 Version doesn't start
-------------------------

The ``EtwCanary`` module is broken and doesn't work on x86 systems. You won't get an appropriate error message. The agent just crashes silently on Windows x86 systems. 

Work Around
~~~~~~~~~~~

Use this flag to start the agent: ``--deactivate-module EtwCanary``

Set this flag in the config file:

.. code:: yaml 

    deactivate-module:
        - EtwCanary

Status
~~~~~~

The module has been temporarily disabled in all configs except ``agent-config-intense.yml`` in build ``4a34c34`` (24.12.2021)

Unknown Flags in Default Configs 
--------------------------------

.. code:: winbatch 

    error while parsing arguments: unknown flag: --no-hashes

.. code:: winbatch 

    module LsaDumpCheck specified as deactivated, but does not exist

Status
~~~~~~

Fixed in build ``71e787c`` (24.12.2021)

Status
~~~~~~

Will be fixed in week 2 of 2022. 

Rule: "Rundll32 Internet Connection" Misses CommandLine Field 
-------------------------------------------------------------

Matches with the rule "Rundll32 Internet Connection" currently miss a ``CommandLine`` field. Adding that field to the rule is already on our list of features. 

Missing Self-Defense
--------------------

- Folder permission checks
- ETW manipulations (the ETW canary module already covers some of them)
- Warning events on configuration changes
