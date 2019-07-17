# Ethical Hacking Notes
___

### Changing your device's MAC Address

- First, ensure device is visible with `ifconfig` or `iwconfig`

- Next, take device down with `ifconfig <device name> down`
 
- Next, change the MAC Address with `ifconfig <device name> hw ether <MAC Address>` where MAC Address follow format 00:00:00:00:00:00

- Lastly, bring the device back online with `ifconfig <device name> up`
___

### Change Wirless Adapter to Utilize Monitor Mode

- First, ensure device is visible and not in monitor mode with `iwconfig`

- Next, bring down the device with `ifconfig <device name> down`

- Next, kill off processes that might interfere with aircrack-ng suit by running `airmon-ng check kill`

- Next, update monitor mode by running `iwconfig <device name> mode monitor`

- Lastly, bring the device back online with `ifconfig <device name> up`
___

### Packet Sniffing Using Airodump-ng

- To start packet sniffing, run `airodump-ng <device name>` where device name is your wireless adapter in monitor mode

- To specify the band frequency, utilize the `--band` argument

   `airodump-ng --band abg <device name>` will capture packets over 2.4 and 5 Ghz simultaniously

- In order to sniff packets on a specific network utilize the below command

   `airodump-ng --bssid <router MAC Address> --channel <channel number> --write <write file> <device name>`

___

### Deauthentication Attack with aireplay-ng

- To disconnect any device from any router utilize the command:

   aireplay-ng --deauth <# of packets> -a <Router MAC> -c <Client MAC> <device name>

**DO NOT DO THIS TO A NETWORK OR DEVICE YOU DO NOT OWN OR HAVE PERMISSION TO...**
   
