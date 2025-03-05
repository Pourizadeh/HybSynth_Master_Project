#-------------------------------------------------------------------------------
# Name:        waveform.py
# Purpose:     Project's waveform generator
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, Square, TriTable, SawTable

class WaveformGenerator:
    def __init__(self, freq=440, mul=0.5):
        self.freq = freq
        self.mul = mul
        self.wave_type = 'sine'
        self.osc = Sine(freq=self.freq, mul=self.mul)

    def update_waveform(self, wave_type, freq, mul):
        self.freq = freq
        self.mul = mul
        if wave_type != self.wave_type:
            self.wave_type = wave_type
            if wave_type == 'sine':
                self.osc = Sine(freq=self.freq, mul=self.mul)
            elif wave_type == 'square':
                self.osc = Square(freq=self.freq, mul=self.mul)
            elif wave_type == 'triangle':
                self.osc = TriTable(freq=self.freq, mul=self.mul)
            elif wave_type == 'sawtooth':
                self.osc = SawTable(freq=self.freq, mul=self.mul)
        else:
            self.osc.freq = self.freq
            self.osc.mul = self.mul

    def get_output(self):
        return self.osc
