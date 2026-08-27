import sounddevice as sd
import numpy as np
import wave
import io
import os


class AudioManager:

    def __init__(self,
                 sample_rate=44100,
                 channels=1):

        self.sample_rate = sample_rate
        self.channels = channels

    # -----------------------------------
    # Record Audio
    # -----------------------------------

    def record(self, duration=5):

        print(f"\nRecording for {duration} seconds...")

        audio = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype=np.int16
        )

        sd.wait()

        print("Recording Finished.")

        return audio

    # -----------------------------------
    # NumPy -> WAV Bytes
    # -----------------------------------

    def audio_to_bytes(self, audio):

        buffer = io.BytesIO()

        with wave.open(buffer, "wb") as wav:

            wav.setnchannels(self.channels)

            wav.setsampwidth(2)

            wav.setframerate(self.sample_rate)

            wav.writeframes(audio.tobytes())

        return buffer.getvalue()

    # -----------------------------------
    # WAV Bytes -> NumPy
    # -----------------------------------

    def bytes_to_audio(self, wav_bytes):

        buffer = io.BytesIO(wav_bytes)

        with wave.open(buffer, "rb") as wav:

            frames = wav.readframes(wav.getnframes())

            audio = np.frombuffer(
                frames,
                dtype=np.int16
            )

            audio = audio.reshape(-1, self.channels)

        return audio

    # -----------------------------------
    # Play Audio
    # -----------------------------------

    def play(self, audio):

        print("\nPlaying Voice...")

        sd.play(
            audio,
            self.sample_rate
        )

        sd.wait()

        print("Playback Finished.")


    def play_last(self):
    
        filename = "received/voice_received.wav"
    
        if not os.path.exists(filename):
    
            print("No received voice available.")
    
            return False
    
        try:
    
            with open(filename, "rb") as file:
                wav_bytes = file.read()
    
            audio = self.bytes_to_audio(wav_bytes)
    
            self.play(audio)
    
            return True
    
        except Exception as e:
    
            print(f"Playback Error: {e}")
    
            return False

    # -----------------------------------
    # Save Received Audio
    # -----------------------------------
    def save_received(self,
                  wav_bytes,
                  filename="received/voice_received.wav"):

      os.makedirs(os.path.dirname(filename), exist_ok=True)

      with open(filename, "wb") as file:
        file.write(wav_bytes)

      print(f"Saved: {filename}")


   