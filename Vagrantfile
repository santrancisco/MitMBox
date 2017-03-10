# -*- mode: ruby -*-
# vi: set ft=ruby :

##################
# NOTE: For handling external devices (USB wifi & ethernet):
# INSTALL VirtualBox Extension Pack (https://www.virtualbox.org/wiki/Downloads)
# Afterward, you can run `VBoxManage list extpacks` and see output similar to below:
# VBoxManage list extpacks
# Extension Packs: 1
# Pack no. 0:   Oracle VM VirtualBox Extension Pack
# Version:      5.1.14
# Revision:     112924
# Edition:
# Description:  USB 2.0 and USB 3.0 Host Controller, Host Webcam, VirtualBox RDP, PXE ROM, Disk Encryption, NVMe.
# VRDE Module:  VBoxVRDP
# Usable:       true
# Why unusable:


##############
require 'yaml'

settings = YAML.load_file("settings.yml")
Vagrant.configure(2) do |config|
config.vm.box = "ubuntu/trusty64"
config.vm.provider "virtualbox" do |vb|
	vb.memory = "1024"
	vb.cpus = "1"
	vb.customize ["modifyvm", :id, "--usb", "on"]
	vb.customize ["modifyvm", :id, "--usbehci", "on"]
	settings["devices"].each do |device|
    if (device["enabled"]) then
      ## The line below is for debug to check condition working as expected
      ## and will runs 3 times because ruby evaluate the file and will execute puts.
      ## Provision only runs once ;)
      puts 'Adding '+ device["name"]+' to Vagrant box'
  		vb.customize ['usbfilter', 'add', '0',
  	        '--target', :id,
  	        '--name', device["name"],
  	        '--vendorid', device["vendorid"],
  	        '--productid', device["productid"]]
    end
	end

#config.vm.network "forwarded_port", guest: 3000, host: 3001, auto_correct: true
# When first started, You should run vagrant up --no-provision
# Then run the playbook vagrant provision --provision-with playbook
# Then run whatever you need for example vagrant provision --provision-with startAP
end
   config.vm.network "private_network", ip: "192.168.33.109"
     config.vm.provision "accesspoint_prepare", type: "ansible" do |ansible|
         ansible.playbook = "accesspoint_prepare.yml"
     end
     config.vm.provision "accesspoint_start", type: "ansible" do |ansible|
         ansible.playbook = "accesspoint_start.yml"
     end
end
