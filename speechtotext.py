import os
from pydub import AudioSegment
import speech_recognition as sr
import subprocess

# Initialize the recognizer
recognizer = sr.Recognizer()

# Paths
opus_directory = "./audios/OPUS/"
wav_directory = "./audios/WAV/"

os.makedirs(wav_directory, exist_ok=True)

for opus_file in os.listdir(opus_directory):
    if opus_file.endswith(".opus"):
        opus_path = os.path.join(opus_directory, opus_file)
        wav_path = os.path.join(wav_directory, opus_file.replace(".opus", ".wav"))

        # Convert OPUS to WAV using ffmpeg subprocess call as a fallback
        conversion_command = ["ffmpeg", "-i", opus_path, wav_path]
        try:
            subprocess.run(conversion_command, check=True)
        except subprocess.CalledProcessError:
            print(f"FFmpeg failed to convert {opus_file}.")
            continue

        # Load the WAV file and transcribe
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            try:
                transcription = recognizer.recognize_google(audio_data, language="pt-BR")
                print(f"Transcription for {opus_file}: {transcription}\n")
            except sr.UnknownValueError:
                print(f"Could not understand the audio in {opus_file}.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
