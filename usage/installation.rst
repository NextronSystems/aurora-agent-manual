Installation
============

Install Aurora
--------------

You can install the agent using the following command line from command line terminal that has been started "As Administrator".

.. code:: winbatch

    aurora-agent.exe --install

After the installation the agent, configuration files and rules reside in ``C:\\Program Files\\Aurora Agent\\``.

It automatically copies all rule files located in a sub folder named ``./rules``. This folder contains the current open source rule set maintained in the `Sigma repository <https://github.com/SigmaHQ/sigma>`__. 

Aurora ships with 4 preset configurations that we encourage you to explorer and use: 

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

If you want to add your own Sigma rules, you can do this by using the ``--rules-path`` flag. If you're using this flag, don't forget to add the path of the built-in rules as well. 

.. code:: winbatch

    aurora-agent.exe --install --rules-path .\rules --rules-path .\my-rules

All the flags that you use after ``--install`` get written to the configuration file named ``agent-config.yml`` in the ``C:\\Program Files\\Aurora Agent\\`` folder and will be used by the service.

A typical command to install Aurora would look like this

.. code:: winbatch

    aurora-agent.exe --install --rules-path .\rules --rules-path .\our-custom-rules --activate-responses

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
