Known Issues
============

AUR#002: Missing ``exclude`` Feature in Aurora Util Lite
--------------------------------------------------------

.. list-table:: 
    :header-rows: 1

    * - Introduced Version
      - Fixed Version
    * - 0.8.0
      - Open

The process exclusion feature that allows to add a process automatically to
the ``conf/process-exclusions.cfg`` automatically is missing in Aurora Lite
Util and only available in the full version. This is an error. 

AUR#001: Missing Self-Defense
-----------------------------

.. list-table:: 
    :header-rows: 1

    * - Introduced Version
      - Fixed Version
    * - N/A
      - Open

- Folder permission checks
- ETW manipulations (the ETW canary module in the full Aurora version already covers some of them)
- Warning events on configuration changes
