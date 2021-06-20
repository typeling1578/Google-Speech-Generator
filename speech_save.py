import pyaudio
import requests
import urllib
import wave

speech_speed = 0.5
speech_lang = "ja"

text = input("text: ")

encode_text = urllib.parse.quote(text)

result = requests.get("https://www.google.com/speech-api/v1/synthesize?text=" + encode_text + "&enc=l16&lang=" + speech_lang + "&speed=" + str(speech_speed) + "&client=lr-language-tts&use_google_only_voices=1")

audio_data = result.content

wavFile = wave.open("test.wav", 'wb')
wavFile.setnchannels(1)
wavFile.setsampwidth(2)
wavFile.setframerate(24000)
wavFile.writeframes(audio_data)
wavFile.close()
