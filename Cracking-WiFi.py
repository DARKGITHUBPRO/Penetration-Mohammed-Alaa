import subprocess
import re
import os
import pystyle
from pystyle import *
from colorama import Fore
from datetime import datetime

# Initialize a log file to save all details
log_file = "pass.txt"

# Log function to save details
def log_details(data):
    with open(log_file, "a", encoding="utf-8") as log:
        log.write(data + "\n")

print("")

# Scan networks using netsh on Windows
def scan_wifi():
    print("[*] Scanning nearby networks...")
    try:
        networks = subprocess.check_output(["netsh", "wlan", "show", "network"], stderr=subprocess.STDOUT)
        networks = networks.decode("latin1", errors='ignore')

        essids = re.findall(r'SSID \d+ : (.*)', networks)
        encryption = re.findall(r'Encryption key\s+:\s+(.*)', networks)
        signal_strength = re.findall(r'Signal\s+:\s+(\d+)', networks)
        bssids = re.findall(r'BSSID \d+ : (.*)', networks)

        if not essids:
            print("[!] No nearby networks found")
            log_details("[!] No nearby networks found")
            return []

        network_info = []
        for index, essid in enumerate(essids):
            encryption_type = encryption[index] if index < len(encryption) else "Open"
            signal = int(signal_strength[index]) if index < len(signal_strength) else 0
            bssid = bssids[index] if index < len(bssids) else "Not available"
            network_info.append((essid, encryption_type, signal, bssid))

        network_info.sort(key=lambda x: x[2], reverse=True)

        log_details("\n[*] Nearby networks :")
        for idx, info in enumerate(network_info, 1):
            network_data = (f"{idx}. Network Name : {profile_name} \n {info[0]}[-] Encryption Type : {info[1]}, "
                            f"\n[-] Signal Strength : {info[2]}%, \n[-] BSSID : {info[3]}")
            print(network_data)
            log_details(network_data)

        return network_info
    except Exception as e:
        error_msg = f"\33[91;1m[!] An Error Occurred : \33[39;0m{e}"
        print(error_msg)
        log_details(error_msg)
        return []


# Get the stored password for a specific network
def get_wifi_password(profile_name):
    print(f"\33[92;1m[-] Retrieving Password For Network \33[39;0m: {profile_name}")
    try:
        command = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        result = result.decode("latin1", errors='ignore')

        password_search = re.search(r"Key Content\s+:\s+(.*)", result)
        if password_search:
            success_msg = f"[+] Password For [{profile_name}] ⇄ [{password_search.group(1)}]"
            print(success_msg)
            log_details(success_msg)
        else:
            no_password_msg = f"\33[91;1m[!] No password found for network \33[39;0m: {profile_name}"
            print(no_password_msg)
            log_details(no_password_msg)
    except subprocess.CalledProcessError:
        error_msg = f"\33[96;2m[!] Could not find password for network \33[39;0m: {profile_name}"
        print(error_msg)
        log_details(error_msg)
    except Exception as e:
        error_msg = f"[!] An error occurred: {e}"
        print(error_msg)
        log_details(error_msg)


# Load password list from an external file
def load_password_list(file_path):
    passwords = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            passwords = file.readlines()
        passwords = [password.strip() for password in passwords]
        log_details(f"[*] Loaded {len(passwords)} passwords from {file_path}")
        return passwords
    except Exception as e:
        error_msg = f"\33[91;1m[!] An Error Occurred While Loading The File \33[39;0m: {e}"
        print(error_msg)
        log_details(error_msg)
        return passwords


# Attempt to guess the password for a network using the stored password list
def test_passwords(profile_name, password_list):
    print(f"\33[3;1m[*] Starting Password Test For Network >| \33[39;0m{profile_name}...")

    for password in password_list:
        test_msg = f"[*] Testing password: {password}"
        print(test_msg)
        log_details(test_msg)
        # Simulated password testing logic here


# Main function to display options to the user
def main():
    Write.Print("Processing....|", Colors.light_red, interval=.01)
    Write.Print("|" * 35, Colors.light_green, interval=0.02)
    print("\n" + "*" * 50)
    print("\33[91;1mWireless Network Hacking Tool\33[39;0m")
    print("*" * 50)

    while True:
        print("\33[96;1m\nAvailable Options:\33[39;0m")
        print("\33[93;1m[01]. Scan nearby networks\33[39;0m")
        print("\33[94;1m[02]. Retrieve WiFi password\33[39;0m")
        print("\33[95;1m[03]. Load password list from a file\33[39;0m")
        print("\33[92;1m[04]. Test passwords on a specific network\33[39;0m")
        print("\33[91;1m[05]. Exit\33[39;0m")
        Write.Print("[**]. Save details as pass.txt\n", Fore.LIGHTWHITE_EX, interval=.01)

        choice = input("\33[93;1m\n[-] Enter The Desired Option \33[39;0m: ")

        if choice == "1":
            networks = scan_wifi()
            if networks:
                print("\33[94;1m[*] You can now select a network to test passwords on.\33[39;0m")

        elif choice == "2":
            network_name = input("\n\33[35;1m[*] Enter The Network Name To Retrieve The Password : \33[39;0m")
            get_wifi_password(network_name)

        elif choice == "3":
            file_path = input("\n\33[94;1m[*] Enter The File Path Containing The Password List : \33[39;0m")
            password_list = load_password_list(file_path)

        elif choice == "4":
            network_name = input("\n\33[96;2m[*] Enter The Network Name To Test Passwords ON : \33[39;0m")
            if 'password_list' in locals():
                test_passwords(network_name, password_list)
            else:
                print("\n\33[91;1m[!] You Must First Load the Password List..\33[39;0m")

        elif choice == "5":
            print("\n[*] Exiting the program.")
            print("\33[94;1m\nDEVELOPER | MOHAMMED ALAA MOHAMMED\n\33[39;0m")
            break

        else:
            print("\n\33[91;1m[!] Invalid Option. Try Again.\33[39;0m")


if __name__ == "__main__":
    main()
