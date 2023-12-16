import string
import hashlib

from entropies.audio import Audio
from entropies.cursor import Cursor
from entropies.disk import Disk
from entropies.display import Display
from entropies.network import Network
from entropies.timer import Timer

from utils.entropy_enhancer import Entropy
from utils.csv_rw import CSVManager

import concurrent.futures


# TODO: need to optimize code for faster speed and lower resource usage.
# TODO: add parameter value checking


class TRNGen:
    def __init__(self, audio=True, a_duration=1, a_samplerate=44100, a_channels=2, disk=True, d_duration=1, cursor=True,
                 display=True, network=True, timer=True, letters=True, digits=True, symbols=True,
                 csv_file_location='dependencies/dataset.csv'):
        self.optional_parameters = {
            'audio': audio,
            'a_duration': a_duration,
            'a_samplerate': a_samplerate,
            'a_channels': a_channels,

            'disk': disk,
            'd_duration': d_duration,

            'cursor': cursor,
            'display': display,
            'network': network,
            'timer': timer,

            'letters': string.ascii_letters if letters is True else letters,
            'digits': string.digits if digits is True else digits,
            'symbols': '!@#$%^&*()_+-=[]{}|;:\'",.<>/?`~' if symbols is True else symbols,

            'csv_file_location': csv_file_location
        }

    def trngen(self):
        op = self.optional_parameters
        # Audio and Disk add delay to code execution for registering in a time interval (DEFAULT 1 second), others are instant
        audio_active, disk_active, cursor_active, display_active, network_active, timer_active = op['audio'], op['disk'], op['cursor'], op['display'], op['network'], op['timer']
        if all(e is False for e in
               (audio_active, disk_active, cursor_active, display_active, network_active, timer_active)):
            raise RuntimeError('Cannot produce random value because all modules are turned off!')
        # Run timer entropy module
        timer = Timer() if timer_active else None
        audio_duration, sample_rate, channels = op['a_duration'], op['a_samplerate'], op['a_channels']
        disk_duration = op['d_duration']

        # Run each entropy module (except Timer) simultaneously using multithread
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(func) for func in (module.return_value for module in [
                Audio(duration=audio_duration, sample_rate=sample_rate, channels=channels) if audio_active else None,
                Disk(interval=disk_duration) if disk_active else None, Cursor() if cursor_active else None,
                Display() if display_active else None, Network() if network_active else None] if
                                                          module is not None)]

            # Wait for threads to end and shutdown executor
            concurrent.futures.wait(futures)
            executor.shutdown()

            # Return and save into list values from every module
            random_values = ([timer.off()] if timer_active else []) + [val.result() for val in futures]

        # XOR and hash combine all values from the 6 different entropy sources
        random_hash = Entropy().extract(*random_values)

        # Save value to dataset.csv file inside dependencies folder
        if location := self.optional_parameters['csv_file_location']:
            CSVManager(location).save_data([random_hash])

        return random_hash

    @staticmethod
    def __int_to_base_n_alpha_string(number, base, charset, length):
        length = length if length else len(str(number))
        result = ''
        while number > 0:
            number, remainder = divmod(number, base)
            result = charset[remainder] + result

        return result[:length]

    def hash(self, algorithm: str = 'sha3_256'):
        if algorithm not in hashlib.algorithms_available:
            raise ValueError(f"Unsupported hash algorithm: {algorithm}")
        hash_algorithm = getattr(hashlib, algorithm)

        return hash_algorithm(str(self.trngen()).encode('utf-8')).hexdigest()

    def percentage(self, simple: bool = False):
        remainder = lambda integer_str: sum(int(digit) for digit in integer_str) % 10
        if hashy := str(self.trngen()):
            floor_div = len(hashy) // 2
            first_half, second_half = remainder(hashy[floor_div:]), remainder(hashy[:len(hashy) - floor_div])
            fractional = hashy[:12] if not simple else ''
            return float('0.' + str(first_half) + str(second_half) + fractional)

    def integer(self, start: int, end: int):
        if random_percentage := self.percentage():
            return int(round((end - start) * random_percentage + start))
        return False

    def float(self, start: int or float, end: int or float):
        if random_percentage := self.percentage():
            return (end - start) * random_percentage + start
        return False

    def alphanumeric(self, length=None):
        if integer_hash := self.trngen():
            op = self.optional_parameters
            charset = ''.join([op['letters'], op['digits'], op['symbols']])
            return self.__int_to_base_n_alpha_string(integer_hash, len(charset), charset, length)
        return ''

    def choice(self, seq: iter):
        if random_percentage := self.percentage():
            index = int(random_percentage * len(seq))
            return seq[index]

    def shuffle(self, seq: iter, in_place=True):
        if not in_place:
            seq = seq.copy()
        for i in range(len(seq) - 1, 0, -1):
            j = self.integer(0, i)
            seq[i], seq[j] = seq[j], seq[i]
        return seq

    def sample(self, seq: iter, sample_size):
        if sample_size > len(seq):
            raise ValueError("Sample size cannot be greater than the collection size.")

        seq_copy = seq.copy()
        self.shuffle(seq_copy)

        return seq_copy[:sample_size]
