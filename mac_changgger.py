#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its Mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Iltimos Interfaceni  kiriting? Tushunmasangiz --help buyrug'ini yozib enterni bosing!")
    elif not options.new_mac:
        parser.error("[-] Iltimos Yangi mac_addressni  kiriting? Tushunmasangiz --help buyrug'ini yozib enterni bosing!")
    return options

def changer_mac(interface,new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

    print("[+] Done! ✅")


options= get_arguments()
changer_mac(options.interface,options.new_mac)

