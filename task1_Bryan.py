from typing import Tuple
import numpy as np
from pulse import Pulse

# CONSTANT DEFINITION
SAMPLING_RATE = 5898.24E6
NS_UNIT = 1E-9
MHZ_UNIT = 1E6

def generate_waveform(pulse: Pulse) :
    """This function generates a waveform array and time sampling point for the given pulse.
    """
    num_samples = int(pulse.duration * SAMPLING_RATE)
    start = pulse.start - (pulse.start % (1.0/SAMPLING_RATE))
    t = (np.arange(num_samples) + start * SAMPLING_RATE )/ SAMPLING_RATE
    waveform = pulse.amplitude * np.sin(2 * np.pi * pulse.frequency * (t) + pulse.phase)
    array = np.array([waveform,t])
    result = tuple(map(tuple,array))
    
    
    return result

# if __name__ == "__main__":

#     generate_waveform(Pulse(
#         start=0,
#         duration=50 * NS_UNIT,
#         frequency=50 * MHZ_UNIT,
#         amplitude=1,
#         phase = 0
#     ))

