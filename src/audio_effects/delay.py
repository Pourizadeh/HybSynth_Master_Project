#-------------------------------------------------------------------------------
# Name:        delay.py
# Purpose:     Initialize the delay effect
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Delay as PyoDelay

class Delay:
    def __init__(self, delay_time=0.1, feedback=0.5):
        self.delay = PyoDelay(input=0, delay=delay_time, feedback=feedback)
        self.input = None  # Store input signal for bypass

    def update_parameters(self, delay_time, feedback):
        self.delay.delay = delay_time
        self.delay.feedback = feedback

    def process(self, input_signal):
        self.input = input_signal  # Save input for bypass
        self.delay.input = input_signal
        return self.delay

    def bypass(self):
        return self.input  # Return original input signal