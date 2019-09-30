import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
print(model_path)
