#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     Project's main code file
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------


import sounddevice as sd
import time

from waveform import SineWave, SquareWave, TriangleWave, SawtoothWave
from effects import Tremolo, Vibrato, Delay
from hardware import Pots, Buttons

samplerate = 44100
duration = 0.1 # Duration of each audio block (in seconds)

def main():
    # Create instances of the waveforms
    sine_wave_gen = SineWave()
    square_wave_gen = SquareWave()
    triangle_wave_gen = TriangleWave()
    sawtooth_wave_gen = SawtoothWave()

    # Create instances of effects
    vibrato_effect = Vibrato(depth=0.1, rate=5)
    tremolo_effect = Tremolo(depth=0.1, rate=5)
    delay_effect = Delay(delay_time=0.1, feedback=0.5)
    
    # Map potentiometer values to desired ranges
    frequency = map_value(freq_value, 0, 1, 100, 10000)
    amplitude = map_value(amp_value, 0, 1, 0, 1)
    delay_time = map_value(delay_time_value, 0, 1, 0.01, 0.5)
    delay_feedback = map_value(delay_feedback_value, 0, 1, 0, 0.9)
    tremolo_depth = map_value(tremolo_depth_value, 0, 1, 0, 0.5)
    tremolo_rate = map_value(tremolo_rate_value, 0, 1, 1, 20)
    vibrato_depth = map_value(vibrato_depth_value, 0, 1, 0, 0.5)
    vibrato_rate = map_value(vibrato_rate_value, 0, 1, 1, 20)


    def map_value(value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    try:
        while True:
            # Generate waveform based on selected switch
            if Buttons.switch_sine_wave.is_pressed:
                processed_wave = sine_wave_gen.generate_wave(duration)
            elif Buttons.switch_square_wave.is_pressed:
                processed_wave = square_wave_gen.generate_wave(duration)
            elif Buttons.switch_triangle_wave.is_pressed:
                processed_wave = triangle_wave_gen.generate_wave(duration)
            elif Buttons.switch_sawtooth_wave.is_pressed:
                processed_wave = sawtooth_wave_gen.generate_wave(duration)

            # Apply effects if enabled
            if Buttons.switch_vibrato.is_pressed:
                processed_wave = vibrato_effect.process(processed_wave)
            else:
                processed_wave = processed_wave
                
            if Buttons.switch_tremolo.is_pressed:
                processed_wave = tremolo_effect.process(processed_wave)
            else:
                processed_wave = processed_wave
                
            if Buttons.switch_delay.is_pressed:
                processed_wave = delay_effect.process(processed_wave)
            else:
                processed_wave = processed_wave
                
            # Read potentiometer values
            freq_value = Pots.pot_frequency.value
            amp_value = Pots.pot_volume.value
            delay_time_value = Pots.pot_delay_time.value
            delay_feedback_value = Pots.pot_delay_feedback.value
            tremolo_depth_value = Pots.pot_tremolo_depth.value
            tremolo_rate_value = Pots.pot_tremolo_rate.value
            vibrato_depth_value = Pots.pot_vibrato_depth.value
            vibrato_rate_value = Pots.pot_vibrato_rate.value

            # Update waveforms parameters
            sine_wave_gen.update_frequency(frequency)
            sine_wave_gen.update_amplitude(amplitude)
            square_wave_gen.update_frequency(frequency)
            square_wave_gen.update_amplitude(amplitude)
            triangle_wave_gen.update_frequency(frequency)
            triangle_wave_gen.update_amplitude(amplitude)
            sawtooth_wave_gen.update_frequency(frequency)
            sawtooth_wave_gen.update_amplitude(amplitude)

            # Update effects parameters
            delay_effect.update_parameters(delay_time, delay_feedback)
            tremolo_effect.update_parameters(tremolo_depth, tremolo_rate)
            vibrato_effect.update_parameters(vibrato_depth, vibrato_rate)

            # Play the processed waveform
            sd.play(processed_wave, samplerate=samplerate)
            sd.wait()

            time.sleep(0.1)  # Short delay to avoid excessive CPU usage

    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()