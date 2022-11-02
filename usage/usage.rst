Usage
=====

This chapter explains some more frequently used command line options used by Aurora in more detail.

Run Aurora
----------

If you simply run Aurora in your terminal, it'll use the default values for each flag and no dedicated config file:

.. code:: doscon
    
    C:\aurora>aurora-agent-64.exe

You can select one of the default config presets with the respective flag:

.. code:: doscon
    
    C:\aurora>aurora-agent-64.exe -c agent-config-reduced.yml

A typical command line that runs Aurora and prints messages and matches to the command line and the Windows ``Application`` eventlog looks like this:

.. code:: doscon 

    C:\aurora>aurora-agent-64.exe --minimum-level low

Run Aurora as Service
---------------------

To install Aurora as a service, use the ``--install`` flag and see the chapter :doc:`installation </usage/installation>` for more details.

A typical installation on systems that have limited hardware resources could look like this. 

.. code:: doscon
    
    C:\aurora>aurora-agent-64.exe --install -c agent-config-reduced.yml

We ship Aurora with 4 presets that we recommend to use. See the chapter :doc:`configuration </usage/configuration>` for more information.

Status Information
------------------

The ``--status`` flag can be used to query status information from the running service.

This flag can be combined with the ``--json`` and ``--trace`` flags for JSON formatted or more detailed output.

.. note::
    If you've set a non-standard name when starting Aurora (using ``--agent-name``), make sure to pass the same value here as well with ``--agent-name``.

.. literalinclude:: ../examples/usage
   :language: doscon
   :linenos:

This flag can be combined with the ``--json`` or ``--trace`` flags:

- JSON output is significantly more comprehensive, but is also more prone to changes (especially additions).
- Trace output contains more details, for example full event statistics.

Tracing Events
--------------

Using the ``--trace`` flag you can view all the events Aurora observes in the different subscribed channels. 

It's a good idea to write the output to a file in order to search in it later. 

.. code:: doscon

    C:\aurora>aurora-agent-64.exe --trace > d:\aurora-trace.log
