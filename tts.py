# Requiements: python3, pip3, espeak, TTS, pygame
# Install steps for TTS: https://github.com/coqui-ai/TTS/discussions/1812
# apt install espeak
# pip install resampy==0.3.1
# Confiuring the audio output device on pi: https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi
from TTS.api import TTS
import pygame

# TTS in english
# Choosing the model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
# Generating the audio
tts.tts_to_file(text="Hello World!", file_path="output.wav")
# Playing the audio
pygame.mixer.init()
sound = pygame.mixer.Sound('./output.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)

# TTS in chinese
# Choosing the model
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False, gpu=False)
# Generating the audio
tts.tts_to_file(text="你好吗？我很好。", file_path="output2.wav")
# Playing the audio
pygame.mixer.init()
sound = pygame.mixer.Sound('./output.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)


