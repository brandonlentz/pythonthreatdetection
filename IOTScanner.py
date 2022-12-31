import socket

# The IP address range to scan
start_ip = '192.168.1.1'
end_ip = '192.168.1.254'

# The port number to scan for unencrypted IOT device traffic
port = 80

# Iterate over the IP address range
for i in range(int(start_ip.split('.')[-1]), int(end_ip.split('.')[-1])+1):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout to prevent the script from hanging indefinitely
    s.settimeout(0.5)
    
    # Get the current IP address to scan
    ip = start_ip[:-1] + str(i)
    
    # Try to connect to the target IP and port
    try:
        s.connect((ip, port))
        print("IoT device found at {ip}:{port}")
    except:
        pass
    
    # Close the socket
    s.close()
