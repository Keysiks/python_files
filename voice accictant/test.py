import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Tell anything")
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-Ru")
print(query.lower())
