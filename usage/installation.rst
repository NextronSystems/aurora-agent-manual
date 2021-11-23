Installation
============

You can install the agent using the following command line from command line terminal that has been started "As Administrator".

.. code:: winbatch

    aurora-agent.exe --install

After the installation the agent and configuration files reside in ``C:\\Program Files\\Aurora Agent\\``.
The Sigma rules and other data reside in ``C:\\ProgramData\\Aurora Agent\\``.

It automatically copies all rule files located in a sub folder named ``./rules``. This folder contains the current open source rule set maintained in the `Sigma repository <https://github.com/SigmaHQ/sigma>`__. 

If you want to add your own Sigma rules, you can do this by using the ``--rules-path`` flag. If you're using this flag, don't forget to add the path of the built-in rules as well. 

.. code:: winbatch

    aurora-agent.exe --install --rules-path .\rules --rules-path .\my-rules

All the flags that you use after ``--install`` get written to the configuration file named ``agent-config.yml`` in the ``C:\\Program Files\\Aurora Agent\\`` folder and will be used by the service.

A typical command to install Aurora would look like this

.. code:: winbatch

    aurora-agent.exe --install --rules-path .\rules --rules-path .\our-custom-rules --activate-responses --auto-reload --minimum-level medium --logfile C:\ProgramData\Aurora-Agent\aurora-events.log

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
    rmdir /s /q "C:\ProgramData\Aurora-Agent"
