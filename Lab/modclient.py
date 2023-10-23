import socket
import pygame
import io


def play_streamed_audio(connection):
    pygame.init()

    try:
        pygame.mixer.init()

        # Initialize an empty audio stream
        audio_stream = io.BytesIO()

        while True:
            data = connection.recv(1024)
            if not data:
                break

            audio_stream.write(data)

        audio_stream.seek(0)  # Reset the stream to the beginning
        pygame.mixer.music.load(audio_stream)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pass  # Wait for the audio to finish playing

    except KeyboardInterrupt:
        pass
    finally:
        pygame.quit()


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    play_streamed_audio(client_socket)

    client_socket.close()


if __name__ == "__main__":
    main()
