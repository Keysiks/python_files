import speech_recognition

if __name__ == "__main__":
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        voice_input = record_and_recognise_audio()
        print(voice_input)

