from typing import Tuple
import numpy as np
from pulse import Pulse
import matplotlib.pyplot as plt

# CONSTANT DEFINITION
SAMPLING_RATE = 5898.24E6
NS_UNIT = 1E-9
MHZ_UNIT = 1E6
MAX_SAMPLES = 65536


buffer = np.zeros(MAX_SAMPLES)
from task1_Bryan import generate_waveform
pulses = [
    Pulse(start=0, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=50e-9, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=1e-6, duration=50e-9, frequency=50e6, amplitude=1, phase=0)
]

for pulse in pulses:
    result = generate_waveform(pulse)

    start_time = result[1][0]
    end_time = result[1][-1]

    print(len(result[1]))
    print(len(result[0]))

    start_index = int(start_time * SAMPLING_RATE)
    end_index = int(end_time * SAMPLING_RATE)

    buffer[start_index:end_index+1] = result[0]

plt.scatter(np.arange(MAX_SAMPLES)/SAMPLING_RATE, buffer)
plt.grid()
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
