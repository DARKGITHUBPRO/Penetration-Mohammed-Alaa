import os
import sys
import time
import pyfiglet
import platform

# Default settings
USER_NAME = "User"  # Default username
LOGO = pyfiglet.figlet_format("PyShell")  # Default logo using pyfiglet
CUSTOM_LOGO = LOGO  # Logo is fixed and cannot be changed by the user
BACKGROUND_COLOR = "\33[48;5;16m"  # Black background
TEXT_COLOR = "\33[97m"  # White text


# Command execution function
def execute_command(command):
    try:
        global USER_NAME  # To modify USER_NAME variable


        # Change username
        if command.startswith("setuser"):
            USER_NAME = command.split(" ")[1]
            print(f"Username changed to {USER_NAME}")
            return

        # Exit command
        elif command == "exit":
            print(f"Goodbye, {USER_NAME}...")
            sys.exit()

        # List files and directories
        elif command == "ls":
            print("\n".join(os.listdir()))  # List current directory content

        # Change directory
        elif command.startswith("cd "):
            os.chdir(command.split(" ")[1])  # Change to the specified directory

        # Show running processes
        elif command == "top":
            os.system("top")  # Display system processes

        # Show interactive process list (if tool is installed)
        elif command == "htop":
            os.system("htop")  # Display processes with interactive interface

        # Show disk usage
        elif command == "df":
            os.system("df -h")  # Display disk usage in human-readable format

        # Show memory usage
        elif command == "free":
            os.system("free -h")  # Display memory usage in human-readable format

        # Show system uptime
        elif command == "uptime":
            os.system("uptime")  # Display system uptime

        # Show network interface details
        elif command == "ifconfig":
            os.system("ifconfig")  # Display network interfaces information

        # Ping command to check connectivity
        elif command == "ping":
            target = input("Enter IP address or domain name to test connectivity : ")
            os.system(f"ping {target}")  # Ping target IP/domain

        # Traceroute to trace the network path
        elif command == "traceroute":
            target = input("Enter IP address or domain name to trace route : ")
            os.system(f"traceroute {target}")  # Trace route to target

        # Show network statistics
        elif command == "netstat":
            os.system("netstat -tuln")  # Display network statistics

        # Use curl to fetch data from a URL
        elif command == "curl":
            url = input("Enter the URL : ")
            os.system(f"curl {url}")  # Fetch data from the URL

        # Download file using wget
        elif command == "wget":
            url = input("Enter the URL to download file from : ")
            os.system(f"wget {url}")  # Download file using wget

        # Clone a Git repository
        elif command == "git":
            repo_url = input("Enter the repository URL : ")
            os.system(f"git clone {repo_url}")  # Clone Git repository

        # Show running processes
        elif command == "ps":
            os.system("ps aux")  # Display running processes

        # Kill a process using PID
        elif command == "kill":
            pid = input("Enter the PID of the process you want to kill : ")
            os.system(f"kill {pid}")  # Kill the process with specified PID

        # Change file permissions
        elif command == "chmod":
            permissions = input("Enter permissions (e.g., 755) : ")
            filename = input("Enter the file name: ")
            os.system(f"chmod {permissions} {filename}")  # Change file permissions

        # Change file owner
        elif command == "chown":
            owner = input("Enter the owner name : ")
            filename = input("Enter the file name : ")
            os.system(f"chown {owner} {filename}")  # Change file owner

        # Execute a command with superuser privileges
        elif command == "sudo":
            command_to_run = input("Enter the command to run with superuser privileges: ")
            os.system(f"sudo {command_to_run}")  # Execute command with sudo

        # Manage firewall using iptables
        elif command == "iptables":
            action = input("Enter the action (e.g., -L, -A) : ")
            os.system(f"sudo iptables {action}")  # Manage firewall with iptables

        # Show manual page for a specific command
        elif command == "man":
            topic = input("Enter the topic to show manual : ")
            os.system(f"man {topic}")  # Show the manual page for a command

        # Display system information
        elif command == "sysinfo":
            system_info()

        # Install package using apt-get (Debian/Ubuntu systems)
        elif command == "apt-get":
            package = input("Enter the package name to install : ")
            os.system(f"sudo apt-get install {package}")  # Install package using apt-get

        # Install package using yum (RedHat/CentOS systems)
        elif command == "yum":
            package = input("Enter the package name to install : ")
            os.system(f"sudo yum install {package}")  # Install package using yum

        # Install package using dnf (Fedora systems)
        elif command == "dnf":
            package = input("Enter the package name to install : ")
            os.system(f"sudo dnf install {package}")  # Install package using dnf

        # Analyze file type
        elif command == "file":
            filename = input("Enter the file name to analyze : ")
            os.system(f"file {filename}")  # Analyze the file type

        # Show file statistics
        elif command == "stat":
            filename = input("Enter the file name to get statistics : ")
            os.system(f"stat {filename}")  # Show file statistics

        # Compress a file using zip
        elif command == "zip":
            file_name = input("Enter the file name to zip : ")
            os.system(f"zip {file_name}.zip {file_name}")  # Compress file using zip

        # Unzip a file
        elif command == "unzip":
            zip_file = input("Enter the zip file name to unzip : ")
            os.system(f"unzip {zip_file}")  # Unzip the file

        # Create a tar file
        elif command == "tar":
            file_name = input("Enter the file name to create a tar from : ")
            os.system(f"tar -cvf {file_name}.tar {file_name}")  # Create tar archive from file

        # Compress a file using gzip
        elif command == "gzip":
            file_name = input("Enter the file name to compress with gzip : ")
            os.system(f"gzip {file_name}")  # Compress file using gzip

        # Show virtual memory statistics
        elif command == "vmstat":
            os.system("vmstat")  # Display virtual memory statistics

        # Clear the screen
        elif command == "clear":
            os.system("clear")  # Clear the terminal screen

        # Show command history
        elif command == "history":
            os.system("history")  # Show the history of executed commands

        # Clear the screen for Windows systems
        elif command == 'cls':
            os.system('cls')  # Clear screen on Windows

        # Show help information
        elif command == "help" or "-h":
            show_help()

        elif command == "run" :
            RUN()
        # Unknown commands
        else:
            os.system(command)  # Execute the command if unknown

    except Exception as e:
        print(f"An error occurred : {e}")


def RUN ():
    start = input("Enter App With Name To Open : ")

    # تحديد النظام (Windows أو Linux)
    if platform.system() == "Windows":
        os.system(f"start {start}")  # فتح البرنامج في Windows
    elif platform.system() == "Linux":
        os.system(app_name)  # فتح البرنامج في Linux
    else:
        print("Unsupported OS")
# Display system information
def system_info():
    print(f"{USER_NAME}, System Information :")
    os.system("uname -a")  # Display kernel information
    os.system("df -h")  # Display disk space usage
    os.system("free -h")  # Display memory usage
    os.system("lscpu")  # Display CPU architecture info
    os.system("uptime")  # Display system uptime


# Show help information
def show_help():
    help_text = """
    PyShell Help:
    ---------------------------
    Available commands:
    - setuser <username>: Change the username.
    - exit: Exit the shell.
    - ls: List files and directories.
    - cd <directory>: Change the directory.
    - clear: Clear the screen.
    - cls: Clear the screen (Windows).
    - top: Show running processes.
    - htop: Show interactive process list (if installed).
    - df: Show disk usage.
    - free: Show memory usage.
    - uptime: Show system uptime.
    - ifconfig: Show network interfaces.
    - ping <target>: Ping to test connectivity.
    - traceroute <target>: Trace route to the target.
    - netstat: Show network statistics.
    - curl <url>: Fetch data from the URL.
    - wget <url>: Download file from URL.
    - git: Clone a Git repository.
    - ps: Show running processes.
    - kill <PID>: Kill a process by PID.
    - chmod <permissions> <file>: Change file permissions.
    - chown <owner> <file>: Change file owner.
    - sudo: Run command with superuser privileges.
    - iptables: Manage firewall.
    - whois <domain>: Lookup domain information.
    - sysinfo: Show system information.
    - apt-get <package>: Install package using apt-get (Debian/Ubuntu).
    - yum <package>: Install package using yum (RedHat/CentOS).
    - dnf <package>: Install package using dnf (Fedora).
    - file <file>: Analyze file type.
    - stat <file>: Show file statistics.
    - zip <file>: Compress file with zip.
    - unzip <file>: Unzip a zip file.
    - tar <file>: Create a tar archive.
    - gzip <file>: Compress file with gzip.
    - vmstat: Show virtual memory statistics.
    - history: Show command history.
    - run: open anyapp
    - help: Show this help message.
    """
    print(help_text)


# Interactive shell function
def interactive_shell():
    print(f"{BACKGROUND_COLOR}{TEXT_COLOR}{CUSTOM_LOGO}")
    print(f"{TEXT_COLOR}Welcome {USER_NAME}! Type 'exit' to exit.")
    while True:
        command = input(f"{USER_NAME}@PyShell:~$ ").lower()  # Get user input and convert to lowercase
        execute_command(command)  # Execute the entered command


# Main function
if __name__ == "__main__":
    print("Welcome to PyShell! Type 'exit' to exit.")
    interactive_shell()  # Start the interactive shell
