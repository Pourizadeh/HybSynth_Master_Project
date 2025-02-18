#-------------------------------------------------------------------------------
# Name:        hardware.py
# Purpose:     Initialize MCP3008 channels for frequency, amplitude,
#              delay feedback, delay time, tremolo depth & tremolo rate
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

from gpiozero import MCP3008, Button

class Pots:
    pot_volume = MCP3008(channel=0)
    pot_frequency = MCP3008(channel=1)
    pot_delay_time = MCP3008(channel=2)
    pot_delay_feedback = MCP3008(channel=3)
    pot_tremolo_depth = MCP3008(channel=4) 
    pot_tremolo_rate = MCP3008(channel=5) 
    pot_vibrato_depth = MCP3008(channel=6)
    pot_vibrato_rate = MCP3008(channel=7)  
    @staticmethod
    def normalize(value, in_min=0, in_max=1, out_min=0, out_max=1):
        """Normalize a value from one range to another."""
        
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Usage example:
volume = Pots.normalize(Pots.pot_volume.value)  # Normalize to 0-1

# ----------------------------------------------------------
# Initialize switches for waveforms and effects
#-----------------------------------------------------------  
class Buttons:
    switch_sine_wave = Button(pin=17, pull_up=True, bounce_time=0.1)
    switch_square_wave = Button(pin=27, pull_up=True, bounce_time=0.1)
    switch_triangle_wave = Button(pin=22, pull_up=True, bounce_time=0.1)
    switch_sawtooth_wave = Button(pin=5, pull_up=True, bounce_time=0.1)
    switch_delay = Button(pin=6, pull_up=True, bounce_time=0.1)
    switch_tremolo = Button(pin=13, pull_up=True, bounce_time=0.1)
    switch_vibrato = Button(pin=19, pull_up=True, bounce_time=0.1)