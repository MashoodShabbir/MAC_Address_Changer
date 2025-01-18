# MAC Address Changer

This Python script allows users to change the MAC address of a specified network interface. It's a useful tool for network troubleshooting, privacy enhancement, or simulating different devices on a network.

## Features

Retrieve the current MAC address of a network interface.

Change the MAC address to a user-specified value.

Validate the format of the new MAC address before applying changes.

Provide clear feedback on the success or failure of the operation.

## Requirements

To run this script, you need:

Python 3.6+

## How to Use

1. Clone the repository or download the script:
```bash
git clone https://github.com/MashoodShabbir/MAC_Address_Changer.git
```

2. Navigate to the directory containing the script:
```bash
cd MAC_Address_Changer
```
Run the script with Python, providing the interface and new MAC address using the -i or --interface and -m or --mac flags:
```bash
python mac_changer.py -i  -m 
```
Example:
```bash
python mac_changer.py -i eth0 -m 00:11:22:33:44:55
```

## Arguments

-i, --interface: Specifies the network interface whose MAC address will be changed. Example: eth0, wlan0.

-m, --mac: Specifies the new MAC address to assign. Must follow the format XX:XX:XX:XX:XX:XX.

## Example Output
```bash
[+] Current MAC = 00:11:22:33:44:55
[+] Changing MAC address for eth0 to 66:77:88:99:AA:BB
[+] New MAC = 66:77:88:99:AA:BB
```
If the MAC address does not change:
```bash
[+] Current MAC = 00:11:22:33:44:55
[+] Changing MAC address for eth0 to 00:11:22:33:44:55
[+] MAC Address was not changed. Please use a different MAC address.
```

## Important Notes

Run as Administrator: This script requires administrative privileges to change the MAC address. Use sudo when running the script if needed.

MAC Address Validation: The script checks if the new MAC address is in the correct format before applying changes. Ensure the MAC address is valid.

Use Responsibly: Ensure you have permission to change the MAC address on the specified interface. Unauthorized changes may violate policies or regulations.

------------------------------------------------------------------------------------------------------------------------------------

Thank you for checking out my project! I hope this script demonstrates my Python skills and interest in networking and cybersecurity.

