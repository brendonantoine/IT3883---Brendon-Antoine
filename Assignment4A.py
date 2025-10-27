# Program Name: Assignment4A.py (use the name the program is saved as)
# Course: IT3883/Section 01
# Student Name: Brendon Antoien
# Assignment Number: Assignment 4A
# Due Date: 10/26/2025
# Purpose: 
# List Specific resources used to complete the assignment.

import socket

# --- Hard-coded Network Parameters ---
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50000        # The port used by the server
BUFFER_SIZE = 1024  # Max size of data to receive

def start_client():
    """Prompts user, connects to server, transmits data, and receives response."""

    # 1. Prompt the user for a string
    user_input = input("Program A (Client): Enter a string to send to the server: ")
    
    # Check if the input is empty
    if not user_input:
        print("Input cannot be empty. Exiting.")
        return

    # 2. Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        try:
            # Connect the socket to the server's host and port
            s.connect((HOST, PORT))
            print(f"Connected to Program B (Server) at {HOST}:{PORT}")
            
            # 3. Transmit the string
            print(f"Sending data: '{user_input}'...")
            s.sendall(user_input.encode('utf-8'))
            
            # 4. Listen for and receive the response
            data = s.recv(BUFFER_SIZE)
            
            # Decode the received bytes back into a string
            received_response = data.decode('utf-8')

            # 5. Print the received response
            print("\n-------------------------------------------------")
            print(f"Response received from Program B (Server): '{received_response}'")
            print("-------------------------------------------------")

        except ConnectionRefusedError:
            print(f"\nError: Could not connect to {HOST}:{PORT}.")
            print("Ensure Program B (the server) is running and listening.")
        except Exception as e:
            print(f"An error occurred in the client: {e}")

if __name__ == "__main__":
    start_client()