from effects import Delay, Tremolo, Vibrato
from waveform import SineWave, SquareWave, TriangleWave, SawtoothWave
from hardware import *

__doc__ = "Waveform generator, audio effects and hardware-related codes"
__all__ =[
    'Delay',
    'Tremolo',
    'Vibrato',
    'SineWave',
    'SquareWave',
    'TriangleWave',
    'SawtoothWave',
    'pot_volume',
    'pot_frequency',
    'pot_delay_time',
    'pot_delay_feedback',
    'pot_tremolo_depth',
    'pot_tremolo_rate',
    'pot_vibrato_depth',
    'pot_vibrato_rate',
    'switch_sine_wave',
    'switch_square_wave',
    'switch_triangle_wave',
    'switch_sawtooth_wave',
    'switch_delay',
    'switch_tremolo',
    'switch_vibrato',
    ]

__version__ = '0.1.0'
__author__ = 'Zahra Pourizadeh'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2025 Zahra Pourizadeh'

