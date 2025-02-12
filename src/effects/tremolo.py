import numpy as np

sample_rate = 44100

class Tremolo:
  def __init__(self, depth=0, rate=5):
    """
    Initialize the Tremolo class with the given depth and rate.

    Parameters
    ----------
    depth : float
        The maximum deviation of the amplitude. Defaults to 0.
    rate : float
        The rate of the tremolo in Hz. Defaults to 5.
    """
    self.depth = depth
    self.rate = rate

  def update_parameters(self, depth, rate):
    self.depth = depth
    self.rate = rate

  def process(self, wave):
    t = np.linspace(0, len(wave) / sample_rate, len(wave))
    tremolo = 1 + self.depth * np.sin(2 * np.pi * self.rate * t)
    return wave * tremolo  # Apply tremolo to the wave