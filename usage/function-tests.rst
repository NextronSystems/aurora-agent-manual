Function Tests
==============

There are easy ways to test Aurora and see if it matches suspicious / malicious events.

Process Creation
----------------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch

    whoami /priv

Network Communication
---------------------

This should create a ``ALERT`` level message for a Sigma rule with level ``critical``.

.. code:: winbatch 

    ping aaa.stage1.123456.test.com

File Creation
-------------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch 

    echo "test" >> C:\temp\lsass.dmp
