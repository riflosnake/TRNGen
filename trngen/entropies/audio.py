import sounddevice as sd
import numpy as np


class Audio:
    def __init__(self, duration, sample_rate, channels):
        self.duration = duration
        self.sample_rate = sample_rate
        self.channels = channels

    @staticmethod
    def sum_audio_samples(audio_data):
        audio_number = np.sum(np.abs(audio_data))
        return audio_number

    def return_value(self):
        audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate=self.sample_rate, channels=self.channels)
        sd.wait()

        return self.sum_audio_samples(audio_data)
