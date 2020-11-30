Fritzbox REST API Implementation
================================

Example Usage:

.. code-block:: python
  with fritzbox(password = 'offline1234') as fritz:

    active_devices = fritz.get_devices(passive = False)

    for device in active_devices:
      print(device)