# MAC_Address_Changer

This is a Python script that allows you to change the MAC address of a network interface on Linux systems. Changing your MAC address can help with network security, anonymity, or troubleshooting network issues.

Features

  Retrieve the current MAC address of a specified network interface.
  
  Validate and change the MAC address to a user-provided value.
  
  Verify that the MAC address was successfully updated.

Usage

  To run the script, use the following syntax:
    sudo python3 mac_changer.py -i <interface> -m <new_mac_address>
  
  Examples
    Change the MAC address of eth0 to 00:11:22:33:44:55:
    sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
  
  Show help information:
    python3 mac_changer.py --help

How It Works

  The script retrieves and displays the current MAC address of the specified network interface.
  
  It validates the new MAC address format before proceeding.
  
  The network interface is brought down, the MAC address is changed, and the interface is brought back up.
  
  The script verifies that the MAC address was successfully updated.

