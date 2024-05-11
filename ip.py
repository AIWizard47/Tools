import socket
import subprocess

def get_ip_address():
    # Get the hostname of the local machine
    hostname = socket.gethostname()
    # Get the IP address corresponding to the hostname

    ip_address = socket.gethostbyname(hostname)
    return [ip_address , hostname]


def get_connected_devices():
    try:
        # Run the arp command to get the list of connected devices
        result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
        output_lines = result.stdout.split('\n')
        
        # Extract the IP addresses from the output
        ip_addresses = []
        for line in output_lines:
            parts = line.split()
            if len(parts) >= 2:
                ip_address = parts[0]
                ip_addresses.append(ip_address)
        
        return ip_addresses
    except Exception as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    print("Your IP Address is:", get_ip_address())
    connected_devices = get_connected_devices()
    print("Connected devices:")
    for ip in connected_devices:
        print(ip)
