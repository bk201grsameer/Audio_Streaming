import socket
import pyaudio

# Define server settings
HOST = "0.0.0.0"  # Use 0.0.0.0 to listen on all available network interfaces
PORT = 12345  # Use any available port you prefer

# Initialize PyAudio
audio = pyaudio.PyAudio()
stream = audio.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=1024,
)

try:
    # Create a TCP socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[+] Listening on {HOST}:{PORT}")

    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f"[+] Accepted connection from {client_address}")

    # Start recording and sending audio data
    print("[+] Recording Started 🎙️")
    print("[+] Press CTRL + C to exit")
    frames = []

    while True:
        data = stream.read(1024)
        frames.append(data)
        client_socket.send(data)  # Send audio data to the connected client

except KeyboardInterrupt:
    print("[+] Stopping the server.")
except Exception as e:
    print(f"[-] An error occurred: {str(e)}")
finally:
    # Clean up resources
    if "client_socket" in locals():
        client_socket.close()
    server_socket.close()
    stream.stop_stream()
    stream.close()
    audio.terminate()
