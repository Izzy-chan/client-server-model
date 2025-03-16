import socket

# Client configuration
HOST = 'localhost'  # Server's IP (same as server's HOST)
PORT = 12345

def main():
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        
        while True:
            # Send message to server
            message = input("\nYou: ").strip()
            client_socket.send(message.encode('utf-8'))
            
            # Check for exit command
            if message.strip().lower() == 'exit':
                print("Exiting...")
                break
            
            # Receive response from server
            response = client_socket.recv(1024).decode('utf-8')
            print(f"\nAdmin: {response}")
            
            # Check if server exited
            if response.strip().lower() == 'exit':
                print("Server disconnected")
                break
    
    except ConnectionRefusedError:
        print("Error: Connection refused. Is the server running?")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
