Responses
=========

Responses are an extension to the Sigma standard used in Aurora agents. 

They can be used to perform certain actions on an event match and therefore immediately respond to a Sigma rule match. Responses can help you contain a threat or limit its damage, but they can also lead to serious problems when they're not handled with care.

WARNING: Only use in cases in which you are absolutely sure that a rule doesn't create false positives and test your custom actions carefully. 

Intended use cases:
   - Worm containment
   - Ransomware containment
   - Hard blocking of certain uses of a tool (otherwise use AppLocker)

Types of Actions
----------------

Aurora agent supports two types of responses:

1. Predefined
2. Custom

The actions can be a list of predefined actions or commands (see examples below).

Predefined Responses
~~~~~~~~~~~~~~~~~~~~

- ``suspend`` (suspends the target process)
- ``kill`` (kills the target process)
- ``dump`` (creates a dump file in folder configured as ``dump-path``)

Custom Responses 
~~~~~~~~~~~~~~~~

A custom response must be a command line calling an executable available from ``PATH``.

You can use the values of fields in the corresponding log line encased with single percent signs (e.g. ``%ProcessId%``).
Windows environment variables can be used encased with double percent signs (e.g. ``%%ProgramData%%``).

Note: Be aware that the variable values correspond to the environment of the Aurora Agent process that runs as SYSTEM and not an observed user process. 

Response flags
--------------

Responses can be modified by a set of flags that are specified within the YAML as key/value structures. The following response flags exist:

Simulate
~~~~~~~~

``simulate`` specifies that a response will not be triggered on a match. Instead, a log entry will be created that notes which response would be triggered. This is the same behaviour as when ``--activate-responses`` is not set.

``simulate`` is supported for all responses.

Recursive
~~~~~~~~~

``recursive`` specifies that a response will also affect all child and descendant processes.

It is supported for the predefined responses and is ``true`` by default.

Low privilege only
~~~~~~~~~~~~~~~~~~

``lowprivonly`` specifies that the response will only be triggered if the target process does not run as ``LOCAL SYSTEM`` or is similarly elevated.

It is supported for the predefined responses and is ``true`` by default.

Ancestor
~~~~~~~~
``ancestors`` specifies that a response will affect a process's ancestor instead of the process itself. ``ancestors: 1`` causes the response to affect the process's parent instead, ``ancestors: 2`` causes it to affect the process's grandparent, and so on.

As a special case, ``ancestors: all`` can be used to affect all ancestors up to the first invalid ancestor (see the ``lowprivonly`` flag).

``ancestors`` is supported for the predefined responses. It is 0 by default.

Process ID field
~~~~~~~~~~~~~~~~
``processidfield`` specifies the field that contains the process ID that shall be affected. 

It is ``ProcessId`` by default and is supported for the predefined responses.

Examples
--------

.. code:: yaml
 
   response:
      type: predefined
      action: kill

Kill the parent process from a process creation event:

.. code:: yaml
 
   response:
      type: predefined
      action: kill
      processidfield: ParentProcessId

Kill the process, the parent and the grandparent:

.. code:: yaml
 
   response:
      type: predefined
      action: kill
      ancestors: 2

.. code:: yaml
 
   response:
      type: predefined
      action: suspend

Copy the executed image to a backup folder, then kill the target process:

.. code:: yaml

   response:
      - type: custom
        action: xcopy %Image% %%ProgramData%%\Aurora\Image-%ProcessID%.bin
      - type: predefined
        action: kill

Simulate a process kill:

.. code:: yaml

   response:
      type: predefined
      action: kill
      simulate: true

Specifying a Response for a Sigma rule
--------------------------------------

Responses can be specified for a Sigma rule in two ways. Both have different advantages and disadvantages.

Inline responses
~~~~~~~~~~~~~~~~

A response can be declared inline in the sigma rule.

This is useful for testing and provides response and sigma rule in a single file. 

However, it is also inflexible since all targets where the sigma rules are deployed will have the same responses active. Also, there is no easy way to list all active responses.

.. code:: yaml

   title: Example rule with inline response
   logsource:
      product: windows
      category: process_creation
   detection:
      selection: 
         Image|endswith: '\example.exe'
      condition: selection
   response:
      type: predefined
      action: kill

Response sets
~~~~~~~~~~~~~

Responses can be declared in a separate `response set` file. This file contains a response in combination with a list of rule IDs that identify the rules where the response should be applied.

Response set files can be passed at startup using the ``--response-set`` option. Multiple response set files can be passed.

If a response is defined in multiple ways for the same rule (e.g. inline and in multiple response sets), the response from the response set that was specified last is used.

.. code:: yaml

   description: My example response set
   response:
      type: predefined
      action: kill
      lowprivonly: true
      ancestors: all
   rule-ids:
      - '87df9ee1-5416-453a-8a08-e8d4a51e9ce1'  # Delete Volume Shadow Copies Via WMI
      - 'ae9c6a7c-9521-42a6-915e-5aaa8689d529'  # CobaltStrike Load by Rundll32

Action Results
--------------

The results of the actions are logged as part of a log message that lists the executed action and the rule that triggered it. This log message is written into the respective output channels. 


