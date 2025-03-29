#-------------------------------------------------------------------------------
# Name:        mcp3008_handler.py
# Purpose:     Handling the mcp3008 ic channels
# Author:      Zahra Pourizadeh
# Created:     03/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

AMPLITUDE_MIN = 0 # The Amplitude knob when Turns down completely
AMPLITUDE_MAX = 1 # The Amplitude knob when Turns down completely

FREQUENCY_MIN = 100 # The Frequency knob when Turns down completely
FREQUENCY_MAX = 4000 # The Frequency knob when Turn up completely

TREMOLO_DEPTH_MIN = 0
TREMOLO_DEPTH_MAX = 0.5
TREMOLO_RATE_MIN = 1
TREMOLO_RATE_MAX = 20

VIBRATO_DEPTH_MIN = 0
VIBRATO_DEPTH_MAX = 0.5
VIBRATO_RATE_MIN = 1
VIBRATO_RATE_MAX = 20

DELAY_TIME_MIN = 0.01
DELAY_TIME_MAX = 0.5
DELAY_FEEDBACK_MIN = 0
DELAY_FEEDBACK_MAX = 0.9

from gpiozero import MCP3008

class MCP3008Handler:
    def __init__(self):
        # Single MCP3008 (8 channels, device=0 for CE0)
        self.mcp = {}
        self.mcp['amp'] = MCP3008(channel=0, device=0)   # Amplitude (0-1)
        self.mcp['freq'] = MCP3008(channel=1, device=0)  # Frequency (100-10000 Hz)
        self.mcp['trem_depth'] = MCP3008(channel=2, device=0)  # Tremolo depth (0-0.5)
        self.mcp['trem_rate'] = MCP3008(channel=3, device=0)   # Tremolo rate (1-20 Hz)
        self.mcp['vib_depth'] = MCP3008(channel=4, device=0)   # Vibrato depth (0-0.5)
        self.mcp['vib_rate'] = MCP3008(channel=5, device=0)    # Vibrato rate (1-20 Hz)
        self.mcp['delay_time'] = MCP3008(channel=6, device=0)  # Delay time (0.01-0.5 s)
        self.mcp['delay_fb'] = MCP3008(channel=7, device=0)    # Delay feedback (0-0.9)

    def map_value(self, value, in_min, in_max, out_min, out_max):
        """Map a value from one range to another."""
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def get_amplitude(self):
        return self.map_value(self.mcp['amp'].value, 0, 1, AMPLITUDE_MIN, AMPLITUDE_MAX)

    def get_frequency(self):
        return self.map_value(self.mcp['freq'].value, 0, 1, FREQUENCY_MIN, FREQUENCY_MAX)

    def get_tremolo_params(self):
        depth = self.map_value(self.mcp['trem_depth'].value, 0, 1, TREMOLO_DEPTH_MIN, TREMOLO_DEPTH_MAX)
        rate = self.map_value(self.mcp['trem_rate'].value, 0, 1, TREMOLO_RATE_MIN, TREMOLO_RATE_MAX)
        return depth, rate

    def get_vibrato_params(self):
        depth = self.map_value(self.mcp['vib_depth'].value, 0, 1, VIBRATO_DEPTH_MIN, VIBRATO_DEPTH_MAX)
        rate = self.map_value(self.mcp['vib_rate'].value, 0, 1, VIBRATO_RATE_MIN, VIBRATO_RATE_MAX)
        return depth, rate

    def get_delay_params(self):
        time = self.map_value(self.mcp['delay_time'].value, 0, 1, DELAY_TIME_MIN, DELAY_TIME_MAX)
        fb = self.map_value(self.mcp['delay_fb'].value, 0, 1, DELAY_FEEDBACK_MIN, DELAY_FEEDBACK_MAX)
        return time, fb
