from os import path
import os
import speech_recognition


def converter_ogg_to_wav(audio_filename):
    import subprocess
    telegram_audio_ogg_wav = f"{audio_filename}.wav"
    telegram_audio_ogg = path.join(path.dirname(path.realpath(__file__)), audio_filename)
    process = subprocess.run(['ffmpeg', '-i', telegram_audio_ogg, telegram_audio_ogg_wav])
    if process.returncode != 0:
        raise Exception("Something went wrong")
    os.remove(audio_filename)
    return telegram_audio_ogg_wav


def converter_audio(audio_filename_ogg):
    audio_filename_wav = converter_ogg_to_wav(audio_filename_ogg)
    return text_recognizer(audio_filename_wav)


def text_recognizer(audio_filename_wav):
    sample_audio = speech_recognition.AudioFile(audio_filename_wav)
    r = speech_recognition.Recognizer()

    with sample_audio as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='ru-RU')
    except speech_recognition.UnknownValueError:
        text = "Извините, не удалось разобрать текст"
    except speech_recognition.RequestError as e:
        text = "Извините Гугл Распозновалка щас не работает; {0}".format(e)
    os.remove(audio_filename_wav)
    return text
