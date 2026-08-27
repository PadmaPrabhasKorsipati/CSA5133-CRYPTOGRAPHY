from audio import AudioManager

audio = AudioManager()

# Record for 5 seconds
recorded = audio.record(5)

# Convert to WAV bytes
wav_bytes = audio.audio_to_bytes(recorded)

print("Bytes Generated :", len(wav_bytes))

# Convert back
restored = audio.bytes_to_audio(wav_bytes)

# Play
audio.play(restored)

# Save
audio.save_received(wav_bytes)