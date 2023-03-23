#### TEST FILE FOR TEXT-TO-SPEECH ####
# espeak, TTS, playsound
# https://github.com/coqui-ai/TTS/discussions/1812
# pip install resampy==0.3.1
from TTS.api import TTS
from playsound import playsound

# Running a multi-speaker and multi-lingual model

# List available 🐸TTS models and choose the first one
model_name = TTS.list_models()[0]
# Init TTS
#tts = TTS(model_name)
# Run TTS
# ❗ Since this model is multi-speaker and multi-lingual, we must set the target speaker and the language
# Text to speech with a numpy output
#wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# Text to speech to a file
#tts.tts_to_file(text="Hello world!", speaker=tts.speakers[0], language=tts.languages[0], file_path="output.wav")
# tts_models/en/ek1/tacotron2
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="Hello World!", file_path="output.wav")
playsound("./output.wav")

# Running a single speaker model

# Init TTS with the target model name
tts = TTS(model_name="tts_models/ja/kokoro/tacotron2-DDC", progress_bar=False, gpu=False)
# Run TTS
#tttts.tts_to_file(text="おはようございます", file_path="output1.wav")
#playsound("./output1.wav")

tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False, gpu=False)
# Run TTS
tts.tts_to_file(text="你好吗？我很好。", file_path="output2.wav")
playsound("./output2.wav")


# Example voice cloning with YourTTS in English, French and Portuguese:
#tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=True)
#tts.tts_to_file("This is voice cloning.", speaker_wav="my/cloning/audio.wav", language="en", file_path="output2.wav")
#tts.tts_to_file("C'est le clonage de la voix.", speaker_wav="my/cloning/audio.wav", language="fr", file_path="output3.wav")
#tts.tts_to_file("Isso é clonagem de voz.", speaker_wav="my/cloning/audio.wav", language="pt", file_path="output4.wav")