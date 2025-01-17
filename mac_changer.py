import subprocess 
import optparse
import re   

def get_args():           
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac Address to assign to the interface")
    (options, arguments) = parser.parse_args()
    if not options.interface and not options.new_mac:
        parser.error("[-] Please specify an interface and a new mac address, use --help for more info")
    elif not options.new_mac: 
        parser.error("[-] Please specify a new mac, use --help for more info")
    elif not options.interface: 
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", options.new_mac):
        parser.error("[-] Invalid MAC address format. Use format like 00:11:22:33:44:55")
    else:
        return options
         
def change_mac(interface, new_mac):   
    print("[+] Changing mac address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface): 
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read the MAC address")
        

options = get_args()

current_mac = str(get_current_mac(options.interface))

print("[+] Current Mac = " + current_mac)

change_mac(options.interface, options.new_mac)

new_mac = str(get_current_mac(options.interface))

if current_mac == new_mac:
    print("[+] MAC Address was not changed. Please use a different MAC address")
else: 
    print("[+] New MAC = " + new_mac)
   
