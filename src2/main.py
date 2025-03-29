#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Project's main code file
# Author:      Zahra Pourizadeh
# Created:     2025
# Copyright:   (c) Zahra Pourizadeh 2025
# License:     MIT
#-------------------------------------------------------------------------------

from pyo import Server
from gpiozero import Button
import time
from .mcp3008_handler import MCP3008Handler
from .waveform import WaveformGenerator
from .audio_effects import Tremolo, Vibrato, Delayed

# ----- Audio Output Characteristics assignments -----
SAMPLE_RATE = 44100
CHANNELS = 2
BUFFER_SIZE = 256
DUPLEX = 0

# ----- GPIO pin assignments -----
TREMOLO_SWITCH_PIN = 17
VIBRATO_SWITCH_PIN = 18
DELAY_SWITCH_PIN = 19
SINE_PIN = 20
SQUARE_PIN = 21
TRIANGLE_PIN = 22
SAWTOOTH_PIN = 23


def main():
    s = Server(sr=SAMPLE_RATE, nchnls=CHANNELS, buffersize=BUFFER_SIZE, duplex=DUPLEX).boot()
    # add '''audio='alsa''' to the Server if needed
    
    # if there are no MIDI input or`` output attached to the project
    # (Like HybSynth v 0.1.0) omit next two lines:
    # s.setMidiInputDevice(999)  # disable MIDI input
    # s.setMidiOutputDevice(999) # # disable MIDI input
    
    s.start()

    # ---   HARDWARE SETUP   ---
    # ---   INITIALIZE SWITCHES   ---

    mcp = MCP3008Handler()
    
    # Effect toggle switches
    tremolo_switch = Button(17, pull_down=True, bounce_time=0.1)  # GPIO17
    vibrato_switch = Button(18, pull_down=True, bounce_time=0.1)  # GPIO18
    delay_switch = Button(19, pull_down=True, bounce_time=0.1)    # GPIO19

    # 4-way waveform selector switches
    sine_switch = Button(20, pull_down=True, bounce_time=0.1)     # GPIO20
    square_switch = Button(21, pull_down=True, bounce_time=0.1)   # GPIO21
    triangle_switch = Button(22, pull_down=True, bounce_time=0.1) # GPIO22
    sawtooth_switch = Button(23, pull_down=True, bounce_time=0.1) # GPIO23
    
    osc = WaveformGenerator()
    tremolo = Tremolo()
    vibrato = Vibrato()
    delay = Delayed()

    # Initialize signal chain
    signal = osc.get_output()
    processed = signal  # Start with dry signal

    try:
        while True:
            # Update waveform
            if sine_switch.is_pressed:
                wave_type = 'sine'
            elif square_switch.is_pressed:
                wave_type = 'square'
            elif triangle_switch.is_pressed:
                wave_type = 'triangle'
            elif sawtooth_switch.is_pressed:
                wave_type = 'sawtooth'
            else:
                wave_type = 'sine'

            freq = mcp.get_frequency()
            amp = mcp.get_amplitude()
            osc.update_waveform(wave_type, freq, amp)
            signal = osc.get_output()

            # Apply effects (with bypass support)
            processed = signal
            if tremolo_switch.is_pressed:
                trem_depth, trem_rate = mcp.get_tremolo_params()
                tremolo.update_parameters(trem_depth, trem_rate)
                processed = tremolo.process(processed)
            
            if vibrato_switch.is_pressed:
                vib_depth, vib_rate = mcp.get_vibrato_params()
                vibrato.update_parameters(vib_depth, vib_rate)
                processed = vibrato.process(processed)
            
            if delay_switch.is_pressed:
                delay_time, delay_fb = mcp.get_delay_params()
                delay.update_parameters(delay_time, delay_fb)
                processed = delay.process(processed)

            processed.out()
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nStopped by user.")
        s.stop()