import socket
import pyaudio

# Define server settings
SERVER_IP = "127.0.0.1"  # Replace with the server's IP address
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

# Create a TCP socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print(f"[+] Connected to {SERVER_IP}:{SERVER_PORT}")

try:
    print("[+] Playing audio 🎵")
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        stream.write(data)  # Play audio data received from the server

except KeyboardInterrupt:
    print("[+] Stopping the client.")
except Exception as e:
    print(f"[-] An error occurred: {str(e)}")
finally:
    # Clean up resources
    client_socket.close()
    stream.stop_stream()
    stream.close()
    audio.terminate()
