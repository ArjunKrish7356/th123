import pyaudio
import wave
import speech_recognition as sr

def transcribe_speech(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        transcribed_text = recognizer.recognize_google(audio_data, language="ml-IN")
        return transcribed_text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""



from mtranslate import translate

def translate_text(text, target_language='en'):
    translation = translate(text, target_language)
    return translation

from pydub import AudioSegment

def convert_webm_to_wav(webm_file, wav_file):
    audio = AudioSegment.from_file(webm_file, format="webm")
    audio.export(wav_file, format="wav")


# Example usage
mp3_file_path = r"c:\Users\91735\Desktop\projects\th-project\backend\temp.webm"
wav_file_path = r"c:\Users\91735\Desktop\projects\th-project\backend\temp.wav"
convert_webm_to_wav(mp3_file_path, wav_file_path)




