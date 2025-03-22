#-------------------------------------------------------------------------------
# Name:        vibrato.py
# Purpose:     Initialize the vibrato effect
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, FreqShift

class Vibrato:
    def __init__(self, depth=0.5, rate=5):
        self.lfo = Sine(freq=rate, mul=depth)
        self.vibrato = FreqShift(input=0, shift=self.lfo)
        self.input = None  # Store input signal for bypass

    def update_parameters(self, depth, rate):
        self.lfo.freq = rate
        self.lfo.mul = depth

    def process(self, input_signal):
        self.input = input_signal  # Save input for bypass
        self.vibrato.input = input_signal
        return self.vibrato

    def bypass(self):
        return self.input  # Return original input signal