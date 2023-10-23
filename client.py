import socket
import pyaudio

# Define server settings
SERVER_IP = "192.168.50.251"  # Replace with the server's IP address
SERVER_PORT = 12345  # Replace with the server's port


# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    output=True,
    frames_per_buffer=1024,
)


def main():
    # create client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((SERVER_IP, SERVER_PORT))
        print(f"[+] CONNECTION SUCCEDED {SERVER_IP}:{SERVER_PORT} ✅ ")
        print("[+] Playing audio 🎵")
        while True:
            data = client.recv(1024)
            if not data:
                break
            stream.write(data)
    except Exception:
        print(" [+] CONNECTION FAILED ❌ ")
        if client:
            client.close()
        stream.stop_stream()
        stream.close()
        audio.terminate()


main()
