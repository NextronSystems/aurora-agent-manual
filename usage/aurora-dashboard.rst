Aurora Agent Dashboard
=================

Aurora Agent Dashboard provides a way to review Aurora Events aswell as get notification Toasts for them:

Running Dashboard
---------------

The Dashboard can be ran either with the installation or live with Aurora with the --dashboard flag:

Examples:

.. code::

   aurora-agent-64.exe --install --dashboard
   aurora-agent-64.exe --dashboard

Opening Dashboard UI
---------------

The Dashboard can be accessed with your favorite browser under the following URL:
``http://localhost:17494/ui/dashboard/overview``

There are also some shortcuts that will open the dashboard such as:
  - Clicking a Notification Balloon
  - Right Clicking the Tray icon and clicking ``Open Dashboard``

Configuring the Notifications
---------------
The filter on which events will create notifications can be configured either in the Tray Icon under ``Options`` or in the Dashboard under the ``Settings``-Section


Other Dashboard Configurations
---------------

General Settings 
~~~~~~~~~~~~~~~~

- Maximum Status Entries

  - Sets the Maximum Status Entries that will be saved in Memory
- Maximum Messages

  - Sets the Maximum Count of Aurora Event Messages that will be saved in Memory

Favorite Fields
~~~~~~~~~~~~~~~
You can set Favorite Fields in the ``Settings`` Section. These Fields will be shown in the Order you set it up in every event you expand. You can change the order by dragging and dropping the Fields in the ``Favorite Fields`` Card
