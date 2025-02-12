import time
import numpy as np
from waveform import SineWave, SquareWave, TriangleWave, SawtoothWave
from effects import Tremolo, Vibrato, Delay
from hardware import Pots, Buttons
from constants import *

# Mapping function
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Initialize waveform generators
sine_wave_gen = SineWave()
square_wave_gen = SquareWave()
triangle_wave_gen = TriangleWave()
sawtooth_wave_gen = SawtoothWave()

# Initialize effects
tremolo_effect = Tremolo(depth=0.1, rate=5)
vibrato_effect = Vibrato(depth=0.1, rate=5)
delay_effect = Delay(delay_time=0.1, delay_feedback=0.5)

# Preallocate buffer for waveform generation
buffer = np.zeros(int(samplerate * duration), dtype=np.float32)

def main():
    
    """Variables to track previous values"""
    
    previous_freq = 0
    previous_amp = 0
    previous_delay_time = 0
    previous_delay_feedback = 0
    previous_tremolo_depth = 0
    previous_tremolo_rate = 0
    previous_vibrato_depth = 0
    previous_vibrato_rate = 0

    try:
        while True:
            # Read potentiometer values
            freq_value = Pots.pot_frequency.value
            amp_value = Pots.pot_volume.value
            delay_time_value = Pots.pot_delay_time.value
            delay_feedback_value = Pots.pot_delay_feedback.value
            tremolo_depth_value = Pots.pot_tremolo_depth.value
            tremolo_rate_value = Pots.pot_tremolo_rate.value
            vibrato_depth_value = Pots.pot_vibrato_depth.value
            vibrato_rate_value = Pots.pot_vibrato_rate.value

            # Update waveform parameters (only if changed)
            if freq_value != previous_freq:
                frequency = map_value(freq_value, 0, 1, frequency_low, frequency_high)
                sine_wave_gen.update_frequency(frequency)
                square_wave_gen.update_frequency(frequency)
                triangle_wave_gen.update_frequency(frequency)
                sawtooth_wave_gen.update_frequency(frequency)
                previous_freq = freq_value

            if amp_value != previous_amp:
                amplitude = map_value(amp_value, 0, 1, amplitude_low, amplitude_high)
                sine_wave_gen.update_amplitude(amplitude)
                square_wave_gen.update_amplitude(amplitude)
                triangle_wave_gen.update_amplitude(amplitude)
                sawtooth_wave_gen.update_amplitude(amplitude)
                previous_amp = amp_value

            # Update effect parameters (only if changed)
            if delay_time_value != previous_delay_time or delay_feedback_value != previous_delay_feedback:
                delay_time = map_value(delay_time_value, 0, 1, delay_time_low, delay_time_high)
                delay_feedback = map_value(delay_feedback_value, 0, 1, delay_feedback_low, delay_feedback_high)
                delay_effect.update_parameters(delay_time, delay_feedback)
                previous_delay_time = delay_time_value
                previous_delay_feedback = delay_feedback_value

            if tremolo_depth_value != previous_tremolo_depth or tremolo_rate_value != previous_tremolo_rate:
                tremolo_depth = map_value(tremolo_depth_value, 0, 1, tremolo_depth_low, tremolo_depth_high)
                tremolo_rate = map_value(tremolo_rate_value, 0, 1, tremolo_rate_low, tremolo_rate_high)
                tremolo_effect.update_parameters(tremolo_depth, tremolo_rate)
                previous_tremolo_depth = tremolo_depth_value
                previous_tremolo_rate = tremolo_rate_value

            if vibrato_depth_value != previous_vibrato_depth or vibrato_rate_value != previous_vibrato_rate:
                vibrato_depth = map_value(vibrato_depth_value, 0, 1, vibrato_depth_low, vibrato_depth_high)
                vibrato_rate = map_value(vibrato_rate_value, 0, 1, vibrato_rate_low, vibrato_rate_high)
                vibrato_effect.update_parameters(vibrato_depth, vibrato_rate)
                previous_vibrato_depth = vibrato_depth_value
                previous_vibrato_rate = vibrato_rate_value

            # Generate waveform based on selected switch
            if Buttons.switch_sine_wave.is_pressed:
                wave = sine_wave_gen.generate_wave(duration, buffer)
            elif Buttons.switch_square_wave.is_pressed:
                wave = square_wave_gen.generate_wave(duration, buffer)
            elif Buttons.switch_triangle_wave.is_pressed:
                wave = triangle_wave_gen.generate_wave(duration, buffer)
            elif Buttons.switch_sawtooth_wave.is_pressed:
                wave = sawtooth_wave_gen.generate_wave(duration, buffer)

            # Apply effects (if enabled)
            if Buttons.switch_tremolo.is_pressed:
                wave = tremolo_effect.process(wave)
            if Buttons.switch_vibrato.is_pressed:
                wave = vibrato_effect.process(wave)
            if Buttons.switch_delay.is_pressed:
                wave = delay_effect.process(wave)

            # Play the processed waveform
            sd.play(wave, samplerate=samplerate)
            time.sleep(duration)  # Wait for the duration of the audio block

    except KeyboardInterrupt:
        print("\nStopped by user.")

if __name__ == "__main__":
    main()