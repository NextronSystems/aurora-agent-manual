Installation
============

You can install the agent using the following command line flag.

.. code:: bash

    aurora-agent.exe --install

The agent and config files will then be installed to ``C:\\Program Files\\Aurora Agent\\``.
The rules and other data will be installed to ``C:\\ProgramData\\Aurora Agent\\``.

It will automatically copy all rule files located in a sub folder named ``./rules``. We ship the agent installer package with the current open source rule set maintained in the `Sigma repository <https://github.com/SigmaHQ/sigma>`__. 

If you want to add your own Sigma rules right during installation, you can do this by using the ``--rules-path`` flag.

.. code:: bash

    aurora-agent.exe --install --rules-path .\rules --rules-path .\my-rules

All the flags that you pass together with  are used for the configuration file ``agent.config``.

.. code:: bash

    aurora-agent.exe --install --rules-path .\rules --rules-path .\my-rules


Uninstall Aurora
----------------

To uninstall the agent simply run the following command:

.. code:: bash 

    aurora-agent.exe --uninstall
