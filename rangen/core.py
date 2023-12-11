import sys

from entropies.audio import Audio
from entropies.cursor import Cursor
from entropies.disk import Disk
from entropies.display import Display
from entropies.network import Network
from entropies.timer import Timer

from utils.error_checker import check
from utils.entropy_enhancer import Entropy

import concurrent.futures

class RanGen:
    def __init__(self, audio=True, a_duration=1, a_samplerate=44100, a_channels=2, disk=True, d_duration=1):
        self.optional_parameters = {
            'audio': audio,
            'a_duration': a_duration,
            'a_samplerate': a_samplerate,
            'a_channels': a_channels,

            'disk': disk,
            'd_duration': d_duration,
        }

    def hash(self):
        op = self.optional_parameters
        # These entropies (audio and disk) add delay to code execution for registering in a time interval (DEFAULT 1 second), others are instant
        audio_active, audio_duration, sample_rate, channels = True if str(op['audio']).lower() == 'true' else False, float(
            op['a_duration']), int(op['a_samplerate']), int(op['a_channels'])
        disk_active, disk_duration = True if str(op['disk']).lower() == 'true' else False, float(op['d_duration'])

        timer = Timer()

        # Run each entropy module (except Timer) simultaneously using multithread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(func) for func in (module.return_value for module in [
                Audio(duration=audio_duration, sample_rate=sample_rate, channels=channels) if audio_active else None,
                Disk(interval=disk_duration) if disk_active else None, Cursor(), Display(), Network()] if
                                                          module is not None)]

            concurrent.futures.wait(futures)
            executor.shutdown()

            random_values = [timer.off()] + [val.result() for val in futures]

        # XOR and hash combine all values from the 6 different entropy sources
        random_hash = Entropy().extract(*random_values)

        return random_hash


if __name__ == "__main__":
    # Initialize RanGen object
    generator = RanGen()
    # Accessing parameters dictionary
    optional_parameters = generator.optional_parameters

    # Check if user has added parameter changes from terminal
    if len(sys.argv) > 1:
        parameters = sys.argv[1:]
        for parameter in parameters:
            key, value = parameter.split('=')
            optional_parameters[key] = value

    # Check for parameter value validity
    check(optional_parameters)

    # Modify parameters
    generator.optional_parameters = optional_parameters

    # Output random hash result
    print(generator.hash())
