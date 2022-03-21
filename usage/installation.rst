Installation
============

Quick Start
-----------

1. Extract the program package into a temporary folder (e.g. C:\aurora-agent)
2. Make sure to place the \*.lic file into the extracted folder
3. Start a cmd.exe as administrator
4. Navigate to the extracted folder
5. Run the following command 

.. code:: winbatch

    aurora-agent.exe --install

6. Verify that new events arrived in the local "Application" event log (Event Viewer)
7. Run the following commands to get details on the current status of the agent 

.. code:: winbatch

    aurora-agent.exe --status 
    aurora-agent.exe --status --trace

Install Aurora
--------------

You can install the agent using the following command line from command line terminal that has been started "As Administrator".

.. code:: winbatch

    aurora-agent.exe --install

After the installation the agent, configuration files and rules reside in ``C:\\Program Files\\Aurora Agent\\``.

It automatically copies all rule files located in a sub folder named ``./signatures/sigma-rules``. This folder contains the current open source rule set maintained in the `Sigma repository <https://github.com/SigmaHQ/sigma>`__. 

Aurora comes with with 4 configuration presets that we encourage you to explore and use: 

- Standard (``agent-config-standard.yml``)
- Reduced (``agent-config-reduced.yml``)
- Minimal (``agent-config-minimal.yml``)
- Intense (``agent-config-intense.yml``)

The different presets are explained in more detail in the chapter :doc:`configuration </usage/configuration>`.

An installation that uses the preset named "reduced" would look like this: 

.. code:: winbatch

    aurora-agent.exe --install -c agent-config-reduced.yml
 
Custom Settings
---------------

Adding your own Sigma rules or IOCs is described in chapter :ref:`custom signatures <Custom Signatures>`. The preferred way is to add them to the ``custom-signatures`` folder before you install Aurora.

All the flags that you use after ``--install`` get written to the configuration file named ``agent-config.yml`` in the ``C:\\Program Files\\Aurora Agent\\`` folder and will be used by the service.

A typical command to install Aurora would look like this

.. code:: winbatch

    aurora-agent.exe --install --activate-responses

Uninstall Aurora
----------------

To uninstall the agent simply run the following command:

.. code:: winbatch 

    aurora-agent.exe --uninstall

If the uninstaller fails due to unknown errors, you can uninstall Aurora manually with these commands 

.. code:: winbatch

    sc stop aurora-agent 
    sc delete aurora-agent
    rmdir /s /q "C:\Program Files\Aurora-Agent"
    schtasks /Delete /F /TN aurora-agent-update
    schtasks /Delete /F /TN aurora-agent-upgrade
