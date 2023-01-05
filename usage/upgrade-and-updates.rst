Upgrading and Updating Aurora
=============================

Management Aurora using ASGARD
------------------------------

When using ASGARD Management Center, you can update Aurora Agent and its signatures for all end systems from the Management Center. 
Doing so is described in more detail in `this <https://asgard-manual.nextron-systems.com/en/latest/usage/administration.html#service-control>`_ section of the ASGARD Management Center manual.

Automatic Updates via Scheduled Tasks 
-------------------------------------

The installer creates two scheduled tasks during the installation of the service. 

One task is scheduled to update the signatures on a daily basis and after each login. The other task is scheduled to update the Aurora agent itself on a weekly basis. Both tasks can be disabled separately. 

.. Note::

    The Aurora agent update also updates the signatures. (``upgrade`` command includes a signature update)


Manual Upgrades and Updates
---------------------------

Aurora Agent Program Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aurora can be upgraded using the Aurora Agent Util binary that is distributed as part of the Aurora Agent package. To upgrade Aurora to the latest version, use:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe upgrade --restart-service

When upgrading Aurora while it is installed, make sure to:

 - Use ``--restart-service`` to automatically stop and start the service (otherwise the service has to be manually stopped and started)
 - Upgrade the installed version using the Aurora Agent Util under ``C:\Program Files\Aurora-Agent``


Signature Updates
^^^^^^^^^^^^^^^^^

When Aurora Agent is installed, it adds a scheduled task that checks daily for signature updates and automatically restarts the service. Usually, this is sufficient and no manual action is necessary.

To manually update Aurora's built-in signatures, use the Aurora Agent Util binary that is distributed as part of the Aurora Agent package:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe update

You can specify ``--auto-reload`` when starting or installing Aurora to automatically reload built-in or custom signatures after you have manually updated them (see the :ref:`usage/configuration:configuration` chapter for more details).

.. code:: doscon

   C:\aurora>aurora-agent-64.exe --install --auto-reload

If you do not use ``--auto-reload``, make sure to restart Aurora for the new signatures to take effect.

If you haven't set ``--auto-reload`` during installation, use the ``--restart-service`` flag to stop and start the service. 

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe update --restart-service 

Update Servers
--------------

Aurora connects to the following Servers to download updates:

- https://update-aurora.nextron-systems.com/
- https://update-lite.nextron-systems.com/

Please ensure that these servers can be reached.