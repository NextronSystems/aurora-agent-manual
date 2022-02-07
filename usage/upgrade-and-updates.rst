Upgrading and Updating Aurora
=============================

Management using ASGARD
-----------------------

When using ASGARD Management Center, you can update Aurora Agent and its signatures for all end systems from the Management Center. 
Doing so is described in more detail in `this <https://asgard-manual.nextron-systems.com/en/latest/usage/administration.html#service-control>`_ section of the ASGARD Management Center manual.

Manual Upgrades and Updates
---------------------------

Aurora Agent Upgrades
^^^^^^^^^^^^^^^^^^^^^

Aurora can be upgraded using the Aurora Agent Util binary that is distributed as part of the Aurora Agent package.
To upgrade Aurora to the latest version, use:

.. code::

   .\aurora-agent-util.exe upgrade

When upgrading Aurora while it is installed, make sure to:

 - Stop the Aurora Agent service
 - Upgrade the installed version using the Aurora Agent Util under ``C:\Program Files\Aurora-Agent``
 - Restart the Aurora Agent service


Signature Updates
^^^^^^^^^^^^^^^^^

When Aurora Agent is installed, it adds a scheduled task that checks daily for signature updates and automatically restarts the service. Usually, this is sufficient and no manual action is necessary.

To manually update Aurora's built-in signatures, use the Aurora Agent Util binary that is distributed as part of the Aurora Agent package:

.. code::

   .\aurora-agent-util.exe update

You can specify ``--auto-reload`` when starting or installing Aurora to automatically reload built-in or custom signatures after you have manually updated them (see the :doc:`configuration </usage/configuration>` chapter for more details):

.. code::

   .\aurora-agent-64.exe --install --auto-reload

If you do not use ``--auto-reload``, make sure to restart Aurora for the new signatures to take effect.
