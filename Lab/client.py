import socket

def receive_file(connection, file_path):
    file_size = int(connection.recv(1024).decode())

    received_data = b''

    while len(received_data) < file_size:
        chunk = connection.recv(1024)
        if not chunk:
            break
        received_data += chunk

    with open(file_path, 'wb') as file:
        file.write(received_data)

def main():
    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    received_file_path = 'received_temp.m4p'  # Replace with your desired file path
    receive_file(client_socket, received_file_path)

    client_socket.close()

if __name__ == "__main__":
    main()
