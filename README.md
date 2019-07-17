# Ethical Hacking Notes
___

### Changing your device's MAC Address

- first, ensure device is visible with `ifconfig` or `iwconfig`

- next, take device down with `ifconfig <device name> down`
 
- next, change the MAC Address with `ifconfig <device name> hw ether <MAC Address>` where MAC Address follow format 00:00:00:00:00:00

- lastly, bring the device back online with `ifconfig <device name> up`
___

### Change Wirless Adapter to Utilize Monitor Mode

- first, ensure device is visible and not in monitor mode with `iwconfig`

- next, bring down the device with `ifconfig <device name> down`

- next, kill off processes that might interfere with aircrack-ng suit by running `airmon-ng check kill`

- next, update monitor mode by running `iwconfig <device name> mode monitor`

- lastly, bring the device back online with `ifconfig <device name> up`

___
