import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the local IP address and port to bind to
local_ip = '127.0.0.1'
local_port = 8080

# Bind the socket to the local IP and port
s.bind((local_ip, local_port))

# Listen for incoming connections
s.listen(5)

# Continuously accept incoming connections and check for threats
while True:
    # Accept an incoming connection
    (client_socket, address) = s.accept()
    
    # Receive data from the client
    data = client_socket.recv(1024)
    
    # Check the data for potential threats
    if data contains "bad_string":
        print("Possible threat detected!")
    
    # Close the client socket
    client_socket.close()

# Close the server socket
s.close()
