# Program Name: Assignment4B.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: Brendon Antoine
# Assignment Number: Assignment 4B
# Due Date: 10/26/2025
# Purpose: This program acts as a server that receives a string from a client, converts it to uppercase, and sends it back.
# List Specific resources used to complete the assignment.

import socket

# --- Hard-coded Network Parameters ---
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50000        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 1024  # Max size of data to receive

def start_server():
    """Starts the server, listens for data, converts to uppercase, and responds."""
    
    # 1. Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            # Bind the socket to the host and port
            s.bind((HOST, PORT))
            
            # Start listening for connections. The argument specifies the max number of queued connections.
            s.listen()
            print(f"Program B (Server) listening on {HOST}:{PORT}...")

            # Accept a new connection
            conn, addr = s.accept()
            with conn:
                print(f"Connected by Program A (Client) at {addr}")
                
                # 2. Receive the data
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    print("Received empty data. Closing connection.")
                    return
                
                # Decode the received bytes into a string
                received_string = data.decode('utf-8')
                print(f"\nReceived from Client: '{received_string}'")

                # 3. Process the data (Convert to uppercase)
                response_string = received_string.upper()
                print(f"Sending response: '{response_string}'")

                # 4. Send the response back to the client
                conn.sendall(response_string.encode('utf-8'))

        except Exception as e:
            print(f"An error occurred in the server: {e}")

if __name__ == "__main__":
    start_server()