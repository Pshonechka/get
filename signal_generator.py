import time
import numpy as np
def get_sin_wave_amplitude(freq, time):
    return (np.sin(2*np.pi*freq*time) + 1)/2
def wait_for_sampling_period(sampling_frequency):
    period = 1/sampling_frequency
    time.sleep(period)