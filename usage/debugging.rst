Debugging
=========

The best way to debug Aurora is to run it directly in the command line and don't use it as service. 

.. code:: bash

    aurora-agent-64.exe --rules-path .\my-rules --debug

The verbosity can even be increased by using the ``--trace`` flag. 

Status Information
------------------

The ``--status`` can give you information from a running Aurora service.

.. code:: bash 

    C:\aurora>aurora-agent-64.exe --status
    Aurora Agent
    Version: 1.0.0
    Sigma Revision: 0.20-1442-g80d2aee9
    Uptime (in hours): 0

    Active Outputs:
    Eventlog: enabled

    Rule Statistics:
    Loaded rules: 723
    Number of rule reloads: 0

    Event Statistics:
    Events observed so far: 1937458
    Events lost so far: 0
    Sigma matches: 23

It displays the number of events that the agent was able to see and process, the number of initialized rules and rule matches. 

Error Messages
--------------

Check the configured log outputs for error messages. A faulty rule would e.g. lead to error messages like this one in the ``Application`` eventlog with EventID 

.. code::

    Could not reload sigma rules 
    Module: Aurora-Agent 
    Changed_files: C:\ProgramData\Aurora-Agent\myrules\my-ransomware.yml 
    Error: could not parse rule response in file "C:\\ProgramData\\Aurora-Agent\\myrules\\my-ransomware.yml": invalid predefined response action kil 
