Installation
============

You can install the agent using the following command line flag.

.. code::bash

    aurora-agent.exe --install

The agent will then be installed to ``C:\\Program Files\\Aurora Agent\\``.

It will automatically install all rule files located in a sub folder named ``./rules``. We ship the agent installer package with the current open source rule set maintained in the ``Sigma repository <https://github.com/SigmaHQ/sigma>`__. 

You can add the same settings as used in the configuration file as command line flags to configure the agent according to your needs. The command line flags will then be added to the configuration file. 

.. code::bash

    aurora-agent.exe --install --eventlog True

Uninstall Aurora
----------------

To uninstall the agent simply run the following command:

.. code::bash 

    aurora-agent.exe --uninstall