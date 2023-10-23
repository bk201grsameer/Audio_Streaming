import pyaudio
import wave


def main():
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=1024,
    )
    try:
        print("[+] Recording Started 🎙️")
        print("[+] Press CTRL + C to exit")
        frames = []
        while True:
            data = stream.read(1024)
            frames.append(data)
            
    except KeyboardInterrupt:
        print("[+] Recording Closed 🔇")
        stream.stop_stream()
        stream.close()
        sound_file = wave.open("myrecording.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        audio.terminate()
        sound_file.close()


main()
