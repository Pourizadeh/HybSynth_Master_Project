#-------------------------------------------------------------------------------
# Name:        delay.py
# Purpose:     initialize the delay effect
# Author:      Zahra Pourizadeh
# Created:     01/01/2025
# Copyright:   (c) Zahra Pourizadeh 2025
# Licence:     MIT
#-------------------------------------------------------------------------------

import numpy as np

sample_rate = 44100

class Delay:
  def __init__(self, delay_time=0.1, delay_feedback=0.5):
    """
    Initialize the Delay class with the given sample rate, delay time, and feedback.

    Parameters
    ----------
    delay_time : float
        The time in seconds for the delay effect. Defaults to 0.1.
    delay_feedback : float
        The amount of delay fed back into the input. Defaults to 0.5.
    """
    self.delay_time = delay_time
    self.delay_feedback = delay_feedback
    self.delay_buffer = np.zeros(int(delay_time * sample_rate))

  def update_parameters(self, delay_time, delay_feedback):
    self.delay_time = delay_time
    self.delay_feedback = delay_feedback
    self.delay_buffer = np.zeros(int(delay_time * sample_rate)) # Reset buffer on parameter change
    
  def process(self, wave):
    delayed_signal = np.roll(self.delay_buffer, len(wave)) 
    output_signal = wave + self.delay_feedback * delayed_signal[:len(wave)]
    self.delay_buffer[:len(wave)] = output_signal
    return output_signal