import time
import os
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

opts = {"names": ("тимофей", "тимоша", "тима", "тим", "тимоха "),
        "tbr": ("скажи", "включи", "сколько", "произнеси"),
        "cmds": {"time": ("время", "сколько время", "скажи время", "время сейчас"),
                 "weather": ("погода сейчас", "какая погода", "скажи погоду", "градусов на улице", "погода в пензе"),
                 "music": ("включи музыку"),
                 "fun": ("рассмеши меня", "расскажи анекдот")}}


def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к тимоше
            cmd = voice

            for x in opts['names']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'time':
        # сказать текущее время
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'weather':
        pass

    elif cmd == 'fun':
        # рассказать анекдот
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")

    else:
        print('Команда не распознана, повторите!')


# запуск тимофея в космос
r = sr.Recognizer()
m = sr.Microphone(device_index=1)

with m as source:
    print('tell anything')
    r.listen(source)

speak_engine = pyttsx3.init()
