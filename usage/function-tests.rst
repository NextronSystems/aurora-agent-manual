Function Tests
==============

There are easy ways to test Aurora and see if it matches suspicious / malicious events.

Sigma Matching
--------------

Sigma Matching - Process Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code-block:: doscon

    C:\Users\nextron>whoami /priv

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code-block:: doscon

    C:\Users\nextron>certutil.exe -urlcache http://test.com

Sigma Matching - Network Communication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``ALERT`` level message for a Sigma rule with level ``critical``.

.. code-block:: doscon 

    C:\Users\nextron>ping aaa.stage.123456.test.com

Sigma Matching - File Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code-block:: doscon 

    C:\Users\nextron>echo "test" > %temp%\lsass.dmp

Sigma Matching - Process Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code-block:: ps1con 

    PS C:\Users\nextron>$id = Get-Process lsass; rundll32.exe C:\Windows\System32\comsvcs.dll , MiniDump $id.Id $env:temp\lsass.dmp full

Cleanup:

.. code-block:: doscon
    
    C:\Users\nextron>del /f %temp%\lsass.dmp

Sigma Matching - Registry
~~~~~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code-block:: doscon 

    C:\Users\nextron>reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /V "AuroraTest" /t REG_SZ /F /D "vbscript"

Cleanup:

.. code-block:: doscon

    C:\Users\nextron>reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /F 

IOC Matching
------------

.. note::
   
   The Aurora Lite version uses only a very limited set of IOCs. 


IOC Matching - Filenames
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: doscon

    C:\Users\nextron>echo "test" > %temp%\loader.ps1

Cleanup: 

.. code-block:: doscon 

    C:\Users\nextron>del %temp%\loader.ps1

IOC Matching - C2 
~~~~~~~~~~~~~~~~~

.. warning:: 

    This could trigger an alert in your internal monitoring (old Sofacy C2)

.. code-block:: doscon 

    C:\Users\nextron>ping drivres-update.info

IOC Matching - Hash 
~~~~~~~~~~~~~~~~~~~

TBD

IOC Matching - NamedPipe
~~~~~~~~~~~~~~~~~~~~~~~~

Start a named pipe using the following PowerShell commands:

.. code-block:: ps1con

    PS C:\Users\nextron>$npipeServer = New-Object System.IO.Pipes.NamedPipeServerStream('testPipe', [System.IO.Pipes.PipeDirection]::InOut)
    PS C:\Users\nextron>$npipeServer.Close()

Included in profiles: Intense

IOC Matching - Mutex
~~~~~~~~~~~~~~~~~~~~

Create a mutex using the following PowerShell commands:

.. code-block:: ps1con

    PS C:\Users\nextron>$mtx = New-Object System.Threading.Mutex($true, "agony")

Matching might take some time (outside of the Intense profile) since mutexes are polled.

CommandLineMismatchDetector
---------------------------

Download Process Ghosting PoC `release package <https://github.com/hasherezade/process_ghosting/releases>`__
named "proc_ghost.zip" by ``@hasherezade``

Extract the package and then run:

.. code-block:: doscon 

    C:\Users\nextron>proc_ghost.exe %comspec% c1.exe

.. note::

    Only available in the full version (not Aurora Lite)
