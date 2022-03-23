Function Tests
==============

There are easy ways to test Aurora and see if it matches suspicious / malicious events.

Sigma Matching
--------------

Process Creation
~~~~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch

    whoami /priv

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch

    certutil.exe -urlcache http://test.com

Network Communication
~~~~~~~~~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``ALERT`` level message for a Sigma rule with level ``critical``.

.. code:: winbatch 

    ping aaa.stage.123456.test.com

File Creation
~~~~~~~~~~~~~

Included in profiles: Minimal, Reduced, Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch 

    echo "test" > %temp%\lsass.dmp

Process Access
~~~~~~~~~~~~~~

Included in profiles: Standard, Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: powershell 

    $id = Get-Process lsass; rundll32.exe C:\Windows\System32\comsvcs.dll , MiniDump $id.Id $env:temp\lsass.dmp full

Cleanup:

.. code:: winbatch
    
    del /f %temp%\lsass.dmp

Registry
~~~~~~~~

Included in profiles: Intense

This should create a ``WARNING`` level message for a Sigma rule with level ``high``.

.. code:: winbatch 

    reg add "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /V "AuroraTest" /t REG_SZ /F /D "vbscript"

Cleanup:

.. code:: winbatch

    reg delete "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\AuroraTest" /F 

IOC Matching
------------

.. note::
   
   The Aurora Lite version uses only a very limited set of IOCs. 


Filenames
~~~~~~~~~

.. code:: winbatch

    echo "test" > %temp%\loader.ps1

Cleanup: 

.. code:: winbatch 

    del %temp%\loader.ps1

C2 
~~

.. warning:: 

    This could trigger an alert in your internal monitoring (old Sofacy C2)

.. code:: winbatch 

    ping drivres-update.info

Hash 
~~~~

TDB

NamedPipe
~~~~~~~~~

TBD

Mutex
~~~~~

TBD

CommandLineMismatchDetector
---------------------------

Download Process Ghosting PoC `release package <https://github.com/hasherezade/process_ghosting/releases>`__ named "proc_ghost.zip" by @hasherezade

Extract the package and then run:

.. code:: winbatch 

    proc_ghost.exe %comspec% c1.exe

.. note::

    Only available in the full version (not Aurora Lite)
