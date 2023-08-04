from dataclasses import dataclass

@dataclass
class Pulse:
    start: float
    duration: float
    frequency: float
    amplitude: int
    phase: float
