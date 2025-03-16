import socket
import sys

# Server configuration
HOST = 'localhost'  # Uses your server's IP for remote access
PORT = 12345

def main():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    
    # Listen for incoming connections (max 1 client)
    server_socket.listen(1)
    print(f"Server is listening on {HOST}:{PORT}")
    
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected by {client_address}")
    
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print("Client disconnected")
                break
            
            print(f"\nClient: {data}")
            
            # Check for exit command
            if data.strip().lower() == 'exit':
                print("Client requested to exit")
                break
            
            # Admin's response
            response = input("Admin: ").strip()
            client_socket.send(response.encode('utf-8'))
            
            # Check if admin wants to exit
            if response.strip().lower() == 'exit':
                print("Admin exiting...")
                break
    
    finally:
        # Close the connections
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
