#-------------------------------------------------------------------------------
# Name:        vibrato.py
# Purpose:     initialize the vibrato effect
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, FreqShift

class Vibrato:
    def __init__(self, depth=0.5, rate=5):
        self.lfo = Sine(freq=rate, mul=depth)
        self.vibrato = FreqShift(input=0, shift=self.lfo)

    def update_parameters(self, depth, rate):
        self.lfo.freq = rate
        self.lfo.mul = depth

    def process(self, input_signal):
        self.vibrato.input = input_signal
        return self.vibrato

    def bypass(self):
        return self.vibrato.input
