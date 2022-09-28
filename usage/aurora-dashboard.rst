Aurora Agent Dashboard
=======================

Aurora Agent Dashboard provides a way to review Aurora events as well as get notifications for them:

.. figure:: ../images/aurora-dashboard-overview.png
   :target: ../images/aurora-dashboard-overview.png
   :alt: Overview Image of dashboard and notification

Running Dashboard
__________________

Aurora can be run or installed with the dashboard feature using the --dashboard flag:

Examples:

.. code::

   aurora-agent-64.exe --install --dashboard
   aurora-agent-64.exe --dashboard

Opening Dashboard UI
_____________________

The Dashboard can be accessed with your favorite browser using the following URL:
`http://localhost:17494/ui/dashboard/overview <http://localhost:17494/ui/dashboard/overview>`_

There are also some shortcuts that will open the dashboard such as:
  - Click on a notification message
  - Right click the tray icon and then ``Open Dashboard``

Configuring the Notifications
------------------------------
The filter for which events will produce notifications can be configured either in the tray icon in the ``Options`` sub menu or in the dashboard in the ``Settings``-section

Settings
_________________
The settings can be accessed in the ``Settings`` Section in the dashboard.

.. figure:: ../images/aurora-dashboard-settings.png
   :target: ../images/aurora-dashboard-settings.png
   :alt: Dashboard settings example


General Settings 
------------------------------

- Maximum Status Entries
   - Sets the Maximum Status Entries that will be saved in Memory
- Maximum Messages
   - Sets the Maximum Count of Aurora Event Messages that will be saved in Memory

Favorite Fields
~~~~~~~~~~~~~~~
You can set favorite fields in the ``Settings`` section. These fields are shown in the configured order in every event you expand. You can change the order by dragging and dropping the fields in the ``Favorite Fields`` list. 
