import socket

# The target IP address and port range to scan
target_ip = '127.0.0.1'
start_port = 1
end_port = 1024

# Iterate over the port range
for port in range(start_port, end_port+1):
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout to prevent the script from hanging indefinitely
    s.settimeout(0.5)
    
    # Try to connect to the target IP and port
    try:
        s.connect((target_ip, port))
        print(f"Port {port} is open")
    except:
        pass
    
    # Close the socket
    s.close()
