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
chinese_text = """
早上好中国。
现在我有冰淇淋。
我很喜欢冰淇淋。
但是 《速度与激情9》。
比冰淇淋。
速度与激情—《速度与激情9》。
我最喜欢。
所以... 现在是音乐时间。
准备。
一二三。

两个礼拜以后。
《速度与激情9》。
两个礼拜以后。
《速度与激情9》。
两个礼拜以后。
《速度与激情9》。


不要忘记 不要错过。
记得去电影院看《速度与激情9》。
因为非常好电影。
动作非常好。
差不多一样冰淇淋。
再见。
"""
tts.tts_to_file(text=chinese_text, file_path="output2.wav")
# Playing the audio
pygame.mixer.init()
sound = pygame.mixer.Sound('./output2.wav')
playing = sound.play()
while playing.get_busy():
    pygame.time.delay(100)


