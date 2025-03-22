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
from .audio_effects import Delay, Tremolo, Vibrato

def main():
    # Initialize Pyo audio server
    
    s = Server().boot()
    
    # The s = Server().boot() command works, but if your speakers 
    # or distortion circuit aren’t picking up the sound, you might
    # need to specify the output device. For example:
    
    # s = Server(audio='alsa', duplex=0).boot()
    
    s.start()
    # Hardware setup
    mcp = MCP3008Handler()
    # Effect switches
    tremolo_switch = Button(17, pull_down=True, bounce_time=0.1)  # GPIO17
    vibrato_switch = Button(18, pull_down=True, bounce_time=0.1)  # GPIO18
    delay_switch = Button(19, pull_down=True, bounce_time=0.1)    # GPIO19
    # 4-way waveform selector
    sine_switch = Button(20, pull_down=True, bounce_time=0.1)     # GPIO20
    square_switch = Button(21, pull_down=True, bounce_time=0.1)   # GPIO21
    triangle_switch = Button(22, pull_down=True, bounce_time=0.1) # GPIO22
    sawtooth_switch = Button(23, pull_down=True, bounce_time=0.1) # GPIO23
    # Waveform and effects
    osc = WaveformGenerator()
    tremolo = Tremolo()
    vibrato = Vibrato()
    delay = Delay()
    signal = osc.get_output()
    processed = signal

    try:
        while True:
            # Update waveform based on 4-way switch
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

            # Apply effects based on switches
            processed = signal
            if tremolo_switch.is_pressed:
                trem_depth, trem_rate = mcp.get_tremolo_params()
                tremolo.update_parameters(trem_depth, trem_rate)
                processed = tremolo.process(processed)
            else:
                processed = tremolo.bypass()
            if vibrato_switch.is_pressed:
                vib_depth, vib_rate = mcp.get_vibrato_params()
                vibrato.update_parameters(vib_depth, vib_rate)
                processed = vibrato.process(processed)
            else:
                processed = vibrato.bypass()
            if delay_switch.is_pressed:
                delay_time, delay_fb = mcp.get_delay_params()
                delay.update_parameters(delay_time, delay_fb)
                processed = delay.process(processed)
            else:
                processed = delay.bypass()
            # Output to speakers (and hardware distortion if connected)
            processed.out()
            time.sleep(0.05)  # Reduce CPU load
    except KeyboardInterrupt:
        print("\nStopped by user.")
        s.stop()

if __name__ == "__main__":
    main()