import numpy as np

sample_rate = 44100

class Vibrato:
  def __init__(self, depth, rate):
    """
    Initialize the Vibrato class with the given sample rate, depth, and rate.

    Parameters:
    ----------
    sample_rate : int
        The sample rate of the audio signal.
    depth : float
        The amplitude of the vibrato effect. Defaults to 0.
    rate : float
        The frequency of the vibrato effect in Hz. Defaults to 5.
    """
    self.depth = depth
    self.rate = rate
    
  def update_parameters(self, depth, rate):
    self.depth = depth
    self.rate = rate

  def process(self, wave):
    t = np.linspace(0, len(wave) / sample_rate, len(wave))
    vibrato = self.depth * np.sin(2 * np.pi * self.rate * t)
    modulated_freq = wave.frequency + vibrato
    return wave.amplitude * np.sin(2 * np.pi * modulated_freq * t)