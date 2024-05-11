import socket
import subprocess

def get_ip_address():
    # Get the hostname of the local machine
    hostname = socket.gethostname()
    # Get the IP address corresponding to the hostname
    ip_address = socket.gethostbyname(hostname)
    return [ip_address , hostname]

def get_device_name(ip_address):
    try:
        # Perform reverse DNS lookup to get the device name
        device_name = socket.gethostbyaddr(ip_address)[0]
        return device_name
    except Exception as e:
        return "Unknown"

def get_connected_devices():
    try:
        # Run the arp command to get the list of connected devices
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')

        # Extract the IP addresses from the output
        devices_info = []
        for line in output_lines:
            parts = line.split()
            if len(parts) >= 2:
                ip_address = parts[0]
                device_name = get_device_name(ip_address)
                devices_info.append((ip_address, device_name))
        return devices_info
    except Exception as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    print("Your IP Address is:", get_ip_address())
    connected_devices = get_connected_devices()
    print("Connected devices:")
    for ip, name in connected_devices:
        print(f"IP Address: {ip}, Device Name: {name}")
