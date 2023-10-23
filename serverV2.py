import socket
import pyaudio
from threading import Thread

exit_flag = False


class Server:
    def __init__(self) -> None:
        # Define server settings
        self.HOST = (
            "192.168.50.251"  # Use the IP to listen on all available network interfaces
        )
        self.PORT = 12345
        # Initialize PyAudio
        self.audio = pyaudio.PyAudio()
        self.stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )
        self.controlThread = None
        self.clientArr = []
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.HOST, self.PORT))
            self.server.listen(1)

        except Exception as ex:
            print("[+] SOCKET INITIALIZATION FAILED ❌")

    def quit_Server(self):
        global exit_flag
        while True:
            quitStr = input("")
            if quitStr == "quit":
                exit_flag = True
                break
            if exit_flag == True:
                break

    def streamAudio(self):
        print("[+] Recording Started 🎙️")
        frames = []
        while True:
            data = self.stream.read(1024)
            frames.append(data)
            try:
                for client in self.clientArr:
                    client.send(data)  # Send audio data to the connected client
            except Exception as ex:
                print(f"[+] SOMETHING WENT WRONG WHILE SENDING AUDIO TO {client}")
                print(str(ex))
                if client in self.clientArr:
                    client.close()
                    self.clientArr.remove(client)
            if exit_flag == True:
                break
        frames = []

    def start(self):
        global exit_flag
        quit_Thread = Thread(target=self.quit_Server)
        quit_Thread.start()

        print(f"[+] Listening on {self.HOST}:{self.PORT} ✅")
        while True:
            self.server.settimeout(1)
            try:
                client, clientaddress = self.server.accept()
                print(f"[+] CONNECTION ACCEPTED FROM {clientaddress}")
                # Start Recording and sending audio data
                self.clientArr.append(client)
                if self.controlThread == None:
                    self.controlThread = Thread(target=self.streamAudio)
                    self.controlThread.start()
            except socket.timeout:
                if exit_flag == True:
                    self.stream.stop_stream()
                    self.stream.close()
                    self.audio.terminate()
                    self.controlThread.join()
                    print("[+] Control_Thread Joined ✅")
                    quit_Thread.join()
                    print("[+] Quit_Thread Joined ✅")
                    print("[-] Streaming Stopped 🔇")
                    break
            except Exception as ex:
                print("[+] SOMETHING WENT WRONG")
                print(str(ex))


def main():
    try:
        server = Server()
        server.start()
    except KeyboardInterrupt:
        print("[-] OPERATION CANCELLED ❌")


if __name__ == "__main__":
    main()
