import pyaudio
import wave

def record_audio(output_file, duration=5, sample_rate=44100, channels=2, chunk_size=1024):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)

    print("Recording complete.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

# Example usage
output_file = r"C:\Users\adith\Downloads\test-path\test1.wav"
record_audio(output_file, duration=10)

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

# Example usage
audio_file_path = output_file
transcribed_text = transcribe_speech(audio_file_path)
print("Transcribed Text:", transcribed_text)


from mtranslate import translate

def translate_text(text, target_language='en'):
    translation = translate(text, target_language)
    return translation

# Example usage
malayalam_text = transcribed_text
english_translation = translate_text(malayalam_text, target_language='en')

print(f"Malayalam: {malayalam_text}")
print(f"English: {english_translation}")


from gtts import gTTS
tts = gTTS(text=transcribed_text, lang='ml')
tts.save('output3.mp3')


