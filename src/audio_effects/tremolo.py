#-------------------------------------------------------------------------------
# Name:        tremolo.py
# Purpose:     initialize the tremolo effect
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, Mix

class Tremolo:
    def __init__(self, depth=0.5, rate=5):
        self.lfo = Sine(freq=rate, mul=depth, add=1-depth)
        self.tremolo = None
        self.input = None  # Store input signal

    def update_parameters(self, depth, rate):
        self.lfo.freq = rate
        self.lfo.mul = depth
        self.lfo.add = 1 - depth

    def process(self, input_signal):
        self.input = input_signal  # Save input for bypass
        self.tremolo = input_signal * self.lfo
        return self.tremolo

    def bypass(self):
        return self.input  # Return original input, not processed signal