Aurora Agent Util
=================

Aurora Agent Util provides utility functions that are not centered around the detection logic:

 - Updating Aurora and its signatures
 - Encrypting custom signatures
 - Excluding "noisy" processes
 - Creating a diagnostics pack with debugging information

Updating Aurora
---------------

There are two commands for Aurora Agent Util to update:

 - ``update`` updates Aurora's signatures. The program files are unaffected and will not be updated.
 - ``upgrade`` upgrades the Aurora fully, both program files and signatures.

Both commands only affect the directory that contains the executable unless ``--restart-service`` is specified.
``--restart-service`` requires Aurora to have been installed with ``--install`` previously and will restart the service
to reload the updated files.

Examples:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe update
   C:\Program Files\Aurora-Agent>aurora-agent-util.exe upgrade --restart-service

Encrypting Signatures
---------------------

You can encrypt your custom signatures (either IOCs or sigma rules) with the ``encrypt`` command
to avoid them being flagged by an Antivirus
or to protect them from hostile reads on a potentially compromised system. Aurora will decrypt them at startup.

The encrypted versions of the passed signatures will be placed next to the unencrypted signatures, with a different
extension.

Encrypted signatures can be passed to Aurora just like unencrypted ones: Via the ``custom-signatures`` folder, or
by specifying them with ``--rules-path`` / ``--ioc-path``.

Examples:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe encrypt path/to/my/sigmarule.yml path/to/my/other/sigmarule.yml

Excluding Processes
-------------------

The ``exclude`` command requires a running Aurora Agent. It will connect to that Agent for status information about
the processes that created the most events and will run a dialogue to comfortably add exclusions for some of these
processes.

Examples:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe exclude

Creating a Diagnostics Pack
---------------------------

The ``diagnostics`` command creates a ZIP file with several files that can be analyzed by us in case of issues. If you encounter an issue, the first step is usually sending us this diagnostics pack along with a description of the issues.

Examples:

.. code:: doscon

   C:\Program Files\Aurora-Agent>aurora-agent-util.exe diagnostics

The diagnostics pack includes the status output, service startup logs (if available) and memory profiles that can be analyzed with the help of `pprof <https://jvns.ca/blog/2017/09/24/profiling-go-with-pprof/>`_.
