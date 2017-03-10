# MitMBox
A box that help attempt to  mitm communication to help me learning Ansible.  

#### Status
 
 - Vagrant + VirtualBox Extension Pack help parsing USB deivces to  
 - Hostapd + DHCPD is working and can quickly create an Accesspoint.
 - Bluez + pibeacon installed to spoof ble beacon 

#### TODO

There are still many things need to be done. But here is some features future me need to work on when i'm free
 
 - grimd dns server (a golang simple dns server) is installed but need a way to configured and get it running as service
 - Optional Moloch for full package capture
 - Binary proxy
 - Firewall rule to bridge networks and let Accesspoint / Ethernet connected device to go out to internet.
 - USB sniffing with Spartan6 FPGA + USB2.0 PHY evaluation board
