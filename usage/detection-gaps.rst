Detection Gaps
==============

Aurora Agent uses ETW to observe a system. However, there are some parts of the system where there are no ETW events or the available events are
not easily usable. Also, an attacker might try to prevent ETW events from reaching Aurora.

Named Pipes
-----------

There is no ETW provider that provides information about creation of or connection to named pipes. The only way to observe named pipe events
is the Kernel Object Handle provider which provides information about all handles that are opened and closed, but which is therefore very "noisy"
and only enabled in the intense configuration. 

To fill this detection gap, Sysmon can be used with e.g. `this configuration <https://github.com/NextronSystems/aurora-helpers/blob/master/sysmon-config/aurora-sysmon-config.xml>`_.

Registry Events
---------------

While there are a couple of ETW providers for registry events such as creating keys or writing values
(primarily ``Microsoft-Windows-Kernel-Registry``), their information is not directly usable. Each event references other keys by their handle, meaning
that all registry handles must be tracked for these events to be useful. Since doing so is fairly expensive in CPU time, Aurora does so in 
the intense configuration, but not in the standard configuration.

The events for setting values here also are apparently broken; while the manifest contains a field for the written data, it appears to be empty.
To query the new value of the registry key, it is necessary to read the registry after receiving the event (which is less reliable since the
value might have been changed again).

.. code::

   EventID:2 Provider_Name:Microsoft-Windows-Kernel-Registry
   BaseName: BaseObject:0xFFFFB700E2344C40 Disposition:0 KeyObject:0xFFFFB700E23442C0
   RelativeName:{34ce6e13-aec9-43ca-a80c-7ee47260ef84} Status:0x0

   EventID:7 Provider_Name:Microsoft-Windows-Kernel-Registry
   CapturedDataSize:0 DataSize:16 InfoClass:2 KeyName: KeyObject:0xFFFFB700E23442C0
   Status:0x0 ValueName:EnableDhcp

   Could not parse event ERROR: "failed to parse \"CapturedData\" value; TdhFormatProperty failed; The parameter is incorrect."

These captured events display the issues here: The first event (with Event ID 2) is an `OpenKey` event. While we see the relative name, the ``BaseName`` field is empty. Therefore, in order to determine the full name of the key, we need to correlate this with previous `OpenKey` events for the key referenced as ``BaseObject``.

The second event (with Event ID 7) is a `QueryValue` event. Again, the ``KeyName`` is empty; instead, the ``KeyObject`` field needs to be correlated with previous `OpenKey` events.
The data that was returned from the `QueryValue` is also missing. There is a field for it, (``CapturedData``) but it is apparently empty based on the ``CapturedDataSize`` and querying its value fails with the displayed error message.

To fill this detection gap, Sysmon can be used with e.g. `this configuration <https://github.com/NextronSystems/aurora-helpers/blob/master/sysmon-config/aurora-sysmon-config.xml>`_.

ETW disabling
-------------

Since ETW events partially originate from user space, an attacker can disable user space ETW events from its own process by patching the syscalls
that Windows uses to create ETW events. Doing so is, in fact, common for attacker frameworks.

While this does not make Aurora useless, you should be aware of this when writing detection rules that are based on these providers.
Usually, any event that originates from the process and is caused by a provider that does not start with ``Microsoft-Windows-Kernel`` can be 
suppressed and should be handled with care.