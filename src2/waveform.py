#-------------------------------------------------------------------------------
# Name:        waveform.py
# Purpose:     Project's waveform generator
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, Osc, TriangleTable, SawTable, SquareTable

class WaveformGenerator:
    def __init__(self, freq=440, mul=0.5):
        self.freq = freq
        self.mul = mul
        self.wave_type = 'sine'
        self.osc = Sine(freq=self.freq, mul=self.mul)
        
        # Precompute tables for waveforms
        self.tri_table = TriangleTable()
        self.saw_table = SawTable()
        self.square_table = SquareTable()

    def update_waveform(self, wave_type, freq, mul):
        self.freq = freq
        self.mul = mul
        if wave_type != self.wave_type:
            self.wave_type = wave_type
            if wave_type == 'sine':
                self.osc = Sine(freq=self.freq, mul=self.mul)
            elif wave_type == 'square':
                self.osc = Osc(table=self.square_table, freq=self.freq, mul=self.mul)
            elif wave_type == 'triangle':
                self.osc = Osc(table=self.tri_table, freq=self.freq, mul=self.mul)
            elif wave_type == 'sawtooth':
                self.osc = Osc(table=self.saw_table, freq=self.freq, mul=self.mul)
        else:
            self.osc.freq = self.freq
            self.osc.mul = self.mul

    def get_output(self):
        return self.osc
