# Audio Streaming in Python using Sockets

This repository demonstrates a simple client-server model for audio streaming in Python using sockets and the PyAudio library. The server captures audio from a microphone and sends it to connected clients, while clients receive and play the audio data in real-time.

## Getting Started

### Prerequisites

To run this code, you'll need Python and the PyAudio library installed on your system. You can install PyAudio using `pip`:

```bash
pip install pyaudio
```

### Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/bk201grsameer/Audio_Streaming.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd Audio_Streaming
   ```

3. Start the server:

   ```bash
   python server.py
   ```

   - The server will begin listening for incoming connections on the specified IP address and port (modify the `HOST` and `PORT` in `server.py`).

4. Start the client:

   ```bash
   python client.py
   ```

   - The client will connect to the server's IP address and port (modify `SERVER_IP` and `SERVER_PORT` in `client.py`).

5. Enjoy audio streaming:
   - The server will capture audio from the microphone and send it to the client.
   - The client will receive and play the audio data in real-time.

6. To stop the server and client, simply press `CTRL + C`.

## Code Explanation

- `server.py`: This script initializes a server, captures audio from the microphone using PyAudio, and sends it to the connected client.

- `client.py`: This script initializes a client, connects to the server, and plays the received audio data using PyAudio.

## Contributing

Contributions to this project are welcome. You can open issues or pull requests to suggest improvements or fix any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyAudio library: https://people.csail.mit.edu/hubert/pyaudio/

Happy audio streaming!
