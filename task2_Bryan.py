import matplotlib.pyplot as plt


from task1_Bryan import generate_waveform
from pulse import Pulse

pulses = [
    Pulse(start=0, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=50e-9, duration=50e-9, frequency=50e6, amplitude=1, phase=0),
    Pulse(start=1e-6, duration=50e-9, frequency=50e6, amplitude=1, phase=0)
]

for pulse in pulses:
    waveform, time_array = generate_waveform(pulse)
    # print(time_array)
    # print(waveform)

    plt.scatter(time_array, waveform)
    plt.grid()
    plt.xlabel("Time [seconds]")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

