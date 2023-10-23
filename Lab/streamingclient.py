import socket


def receive_and_stream_file(connection):
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(data.decode(), end="")


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    receive_and_stream_file(client_socket)

    client_socket.close()


if __name__ == "__main__":
    main()
