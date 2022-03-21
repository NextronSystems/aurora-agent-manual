Custom Signatures
=================

Management using ASGARD
-----------------------

ASGARD Management Center allows you to create rule sets of sigma rules and apply them to groups of end systems. It also features a "difference view" that shows you rules that have changed in the remote Sigma repository and allows you to accept or deny the changes. It also provides ways to filter false positives right at the source.

Signature updates and Aurora upgrades can be executed for all end points from the Management Center.

.. figure:: ../images/asgard-rule-management.png
   :target: ../images/asgard-rule-management.png
   :alt: Asgard Rule Management

The rule management is described in more detail in `this <https://asgard-manual.nextron-systems.com/en/latest/usage/administration.html#service-control>`_ section of the ASGARD Management Center manual.

Manual signature management
---------------------------

Signatures can be specified when starting Aurora using the ``--rules-path`` and ``--ioc-path`` parameters. These parameters default to the built-in rules and IOCs at 
``signatures/sigma-rules`` and ``signatures/iocs`` and the provided paths for custom signatures at ``custom-signatures/sigma-rules`` and ``custom-signatures/iocs`` respectively. 
Aurora traverses the directories that are specified with these parameters recursively and initializes all signature files it finds.

In order to add new sigma rules or IOCs, you can either:

 - Add them to the corresponding subfolder in `custom-signatures`
 - Specify the folder where they are located using ``--rules-path`` or ``--ioc-path``

.. warning::
   If you specifiy ``--rules-path`` or ``--ioc-path``, if you want to use the Aurora built-in rules and IOCs,
   you need to add them manually as well. E.g.:

    .. code:: winbatch

        aurora-agent.exe --install --rules-path .\signatures\sigma-rules --rules-path .\my-rules

    If paths are configured, only the configured paths are used.

Signature format
^^^^^^^^^^^^^^^^

IOCs follow the same format that THOR IOCs do; the full description can be found in the `THOR manual <https://thor-manual.nextron-systems.com/en/latest/usage/custom-signatures.html#simple-iocs>`_.

Sigma rules must adhere to the specification found in the `Sigma repository <https://github.com/SigmaHQ/sigma/wiki/Specification>`_.

Encrypted signatures
^^^^^^^^^^^^^^^^^^^^
Both IOCs and sigma rules can be encrypted using the ``encrypt`` function in Aurora Agent Util. Aurora will automatically decrypt encrypted signatures at startup. 
This functionality is only available in the full version of Aurora.
