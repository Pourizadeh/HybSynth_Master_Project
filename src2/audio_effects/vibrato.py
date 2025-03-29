#-------------------------------------------------------------------------------
# Name:        vibrato.py
# Purpose:     Initialize the vibrato effect
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Sine, Delay

class Vibrato:
    def __init__(self, depth=0.005, rate=5):  # depth in seconds (e.g., 5ms)
        self.lfo = Sine(freq=rate, mul=depth, add=depth)
        self.delay = Delay(input=0, delay=self.lfo)
        self.input_signal = None

    def update_parameters(self, depth, rate):
        self.lfo.freq = rate
        self.lfo.mul = depth
        self.lfo.add = depth  # Center around 'depth' (e.g., 0.005s)

    def process(self, input_signal):
        self.input_signal = input_signal
        self.delay.input = input_signal
        return self.delay

    def bypass(self):
        return self.input_signal