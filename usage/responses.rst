Responses
=========

Responses are an extension to the Sigma standard used in Aurora agents. 

They can be used to perform certain actions on an event match and therefore immediately respond to a Sigma rule match. Responses can help you contain a threat or limit its damage, but they can also lead to serious problems when they're not handled with care.

WARNING: Only use in cases in which you are absolutely sure that a rule doesn't create false positives and test your custom actions carefully. 

Intended use cases:
   - Worm containment
   - Ransomware containment
   - Hard blocking of certain uses of a tool (otherwise sue AppLocker)

Types of Actions
----------------

Aurora agent supports two types of responses:

1. Predefined
2. Custom

The actions can be a list predefined actions or commands. (see examples below)

Predefined Responses
--------------------

- suspend (all events with 'ProcessId', recursive - suspends all children)
- kill (all events with 'ProcessId', recursive - kills all children)
- killparent (all events with 'ParentProcessId', recursive - kills all children)
- dump (all events with 'ProcessId', creates dump file in folder configured as ``dump-path``)

Examples
~~~~~~~~

.. code:: yaml
 
   response:
      type: predefined 
      action: kill

Kill the process and the parent.

.. code:: yaml
 
   response:
      type: predefined 
      action: kill
      ancestors: 1

Kill the process, the parent and the grandparent.

.. code:: yaml
 
   response:
      type: predefined 
      action: kill
      ancestors: 2

.. code:: yaml
 
   response:
      type: predefined 
      action: suspend

.. code:: yaml
 
   response:
      type: custom 
      action: 
         - copy %Image% %%ProgramData%%\aurora-samples\%ProcessId%.bin
         - taskkill /F /PID %ProcessId%

Custom Responses 
----------------

A custom response is standard command line executed as ``cmd.exe /c custom-command``.

You can use the values of fields in the corresponding log line encased with single percent signs (e.g. ``%ProcessId%``).
Windows environment variables can be used encased with double percent signs (e.g. ``%%ProgramData%%``).

Note: Be aware that the variable values correspond to the environment of the Aurora Agent process that runs as SYSTEM and not an observed user process. 

.. code:: yaml

   response:
      type: custom
      action: cmd.exe /c copy %Image% %%ProgramData%%\Aurora\sample-exports\Image-%ProcessID%.bin
