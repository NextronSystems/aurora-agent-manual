Rule Management
===============

The rules used by Aurora are stored in ``C:\Program Files\Aurora-Agent\rules`` unless you've used a different agent name with the ``--agent-name`` command line flag. In the free Aurora Lite version, you have to update and manage the rules manually.

There are two ways to update the rules that the currently running Aurora agent uses:

1. You edit / update the rules in the source folders and reinstall the agent
2. You edit / update the rules in the target folder and restart the service 

(e.g. source folder = ``C:\aurora``, target folder = ``C:\Program Files\Aurora-Agent\rules``)

Rule Management with ASGARD
---------------------------

ASGARD Management Center allows you to create rule sets of sigma rules and apply them to groups of end systems. It also features a "difference view" that shows you rules that have changed in the remote Sigma repository and allows you to accept or deny the changes. It also provides ways to filter false positives right at the source.

.. figure:: ../images/asgard-rule-management.png
   :target: ../images/asgard-rule-management.png
   :alt: Asgard Rule Management

The rule management is described in more detail in `this <https://asgard-manual.nextron-systems.com/en/latest/usage/administration.html#service-control>`_ section of the ASGARD Management Center manual.
