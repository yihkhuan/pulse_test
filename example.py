import matplotlib.pyplot as plt
import numpy as np


from pulse import Pulse


# CONSTANT DEFINITION
SAMPLING_RATE = 6666.24E6
NS_UNIT = 1E-9
MHZ_UNIT = 1E6


# First, we create a pulse
pulse1 = Pulse(
    start= 70 * NS_UNIT,
    duration=70 * NS_UNIT,
    frequency=50 * MHZ_UNIT,
    amplitude=1,
    phase = 0
)

# This pulse plays from t=0 to t=50ns with a frequency of 50MHz
# Next, we want to convert this pulse into samples for our device to play

# First we allocate memory up to the number of samples to be played
num_samples = int(pulse1.duration * SAMPLING_RATE)
buffer = np.zeros(num_samples)

# The waveform at time t of a pulse is amplitude * sin(2 * pi * frequency * t + phase)
# Our instrument can only play samples at discrete time intervals given by the sampling rate

t = (np.arange(num_samples) + int(pulse1.start * SAMPLING_RATE)) / SAMPLING_RATE
# buffer = pulse1.amplitude * np.sin(2 * np.pi * pulse1.frequency * t + pulse1.phase)
buffer = 0 if t<pulse1.start else pulse1.amplitude * np.sin(2 * np.pi * pulse1.frequency * t + pulse1.phase)

plt.scatter(t, buffer)
plt.grid()
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.show()
