#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import os

import librosa  # pip install librosa


def getstarterdir():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


path = os.path.join(getstarterdir(), "data", "file3.flac")
data = librosa.to_mono(librosa.load(path)[0])
stft = librosa.stft(data)

print(stft)
print(len(stft))
