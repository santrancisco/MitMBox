#!/bin/bash
#Initial wifi interface configuration
sudo ifdown $1
sudo killall hostapd
sudo killall dhcpd
sudo ifconfig $1 up 12.0.0.1 netmask 255.255.255.0
sleep 3
###########Start DHCP, comment out / add relevant section##########
#Thanks to Panji
#Doesn't try to run dhcpd when already running
 #start hostapd

hostapd $2 -B
###########
#Enable NAT
if [ "$(ps -e | grep dhcpd)" == "" ]; then
	echo "run dhcpd"
	sudo rm /etc/dhcp/dhcpd.conf
	sudo ln -s /home/remnux/dhcpd_wifi.conf /etc/dhcp/dhcpd.conf
	dhcpd $1 &
fi

sysctl -w net.ipv4.ip_forward=1
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables --table nat --append POSTROUTING --out-interface eth0 -j MASQUERADE
iptables --append FORWARD --in-interface $1 -j ACCEPT

 #Thanks to lorenzo
 #Uncomment the line below if facing problems while sharing PPPoE, see lorenzo's comment for more details
 #iptables -I FORWARD -p tcp --tcp-flags SYN,RST SYN -j TCPMSS --clamp-mss-to-pmtu
echo "Connect to sanpentest with password: butterisuberfat2051"
echo "download burp.crt to your Android at 12.0.0.1/burp.crt"
echo "or go to: http://burp"
echo "To check what's connecting:"
echo "cat /var/lib/dhcp/dhcpd.leases"
