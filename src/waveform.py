#-------------------------------------------------------------------------------
# Name:        waveform.py
# Purpose:     Generate and play audio waves.
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

import numpy as np
import sounddevice as sd

sample_rate = 44100

class WaveForm:
    def __init__(self, frequency=440, amplitude=0.5, phase=0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase  # Add phase initialization

    def generate_wave(self, duration):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = self.amplitude * np.sin(2 * np.pi * self.frequency * t + self.phase)
        return wave

    def play_wave(self, duration):
        wave = self.generate_wave(duration)
        sd.play(wave, samplerate=sample_rate)
        sd.wait()  # Wait until the sound has finished playing

    def update_frequency(self, frequency):
        self.frequency = frequency

    def update_amplitude(self, amplitude):
        self.amplitude = amplitude

class SineWave(WaveForm):
    def generate_wave(self, duration):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = self.amplitude * np.sin(2 * np.pi * self.frequency * t + self.phase)
        return wave

class SquareWave(WaveForm):
    def generate_wave(self, duration):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = self.amplitude * np.sign(np.sin(2 * np.pi * self.frequency * t + self.phase))
        return wave

class TriangleWave(WaveForm):
    def generate_wave(self, duration):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = self.amplitude * (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * self.frequency * t + self.phase))
        return wave

class SawtoothWave(WaveForm):
    def generate_wave(self, duration):
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        wave = self.amplitude * (2 * (t * self.frequency - np.floor(t * self.frequency + 0.5)))
        return wave