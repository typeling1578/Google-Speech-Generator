import pyaudio
import requests
import urllib

speech_speed = 0.5
speech_lang = "ja"

text = input("text: ")

encode_text = urllib.parse.quote(text)

result = requests.get("https://www.google.com/speech-api/v1/synthesize?text=" + encode_text + "&enc=l16&lang=" + speech_lang + "&speed=" + str(speech_speed) + "&client=lr-language-tts&use_google_only_voices=1")

audio_data = result.content
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)
stream.write(audio_data)
stream.stop_stream()
stream.close()
p.terminate()
