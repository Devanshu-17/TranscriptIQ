from pydub import AudioSegment

def convert_to_mp3(audio_file, path):
    # Load the audio file using pydub
    audio = AudioSegment.from_file(audio_file)

    # Export the audio to MP3 format
    audio.export(f"{path}/my_audio1.mp3", format="mp3")