#-------------------------------------------------------------------------------
# Name:        distortion.py
# Purpose:     initialize the distortion effect
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

class Distortion:
    def __init__(self, gain=0.5, tone=0.5):
        # Hardware-based distortion; parameters are for reference only
        self.gain = gain
        self.tone = tone

    def update_parameters(self, gain, tone):
        self.gain = gain
        self.tone = tone
        # No software processing; audio routed to hardware circuit

    def process(self, input_signal):
        # Return input unchanged; hardware handles distortion
        return input_signal

    def bypass(self):
        return input_signal
