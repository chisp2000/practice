import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt


filename = librosa.ex('trumpet')
y, sr = librosa.load(filename)
