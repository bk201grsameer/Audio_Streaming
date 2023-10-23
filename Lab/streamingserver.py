import socket
import os


def stream_file(connection, file_path):
    with open(file_path, "rb") as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            connection.send(data)


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)  # Listen for a single client

    print(f"Server is listening on {server_ip}:{server_port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    file_to_stream = "temp.m4a"  # Replace with your file path
    stream_file(client_socket, file_to_stream)

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    main()
