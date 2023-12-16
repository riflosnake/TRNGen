import hashlib
from random import seed, shuffle, sample


class Entropy:
    def __init__(self):
        self.result = 0
        self.fractional_result = []

    def xor_combine(self, *values):
        for value in values:
            self.fractional_result.append(value % 1)
            self.result ^= int(value)
        return self.result

    @staticmethod
    def hash_combine(*values):
        combined_data = ''.join(str(value) for value in values).encode('utf-8')
        hashed_result = hashlib.sha256(combined_data).hexdigest()
        return int(hashed_result, 16)

    @staticmethod
    def sum_fractional(fractions):
        return sum(
            [int(fraction * 10 ** len(str(fraction).split('.')[1])) if fraction != 0 else 0 for fraction in fractions])

    def deviate_linearity(self, integer):
        integer_string = str(integer)

        length_of_int_str = len(integer_string)
        indices_of_int_str = range(length_of_int_str)

        ran_seed = self.sum_fractional(self.fractional_result)
        first_batch_length = length_of_int_str // 2
        seed(ran_seed)
        first_batch_indices = sample(indices_of_int_str, first_batch_length)

        first_batch = [integer_string[index] for index in first_batch_indices]
        second_batch = [integer_string[index] for index in indices_of_int_str if index not in first_batch_indices]

        seed(ran_seed * first_batch_length)
        shuffle(first_batch)
        first_batch_int = ''.join(first_batch)

        seed(first_batch_int)
        shuffle(second_batch)
        second_batch_int = ''.join(second_batch)

        return int(first_batch_int + second_batch_int)

    def extract(self, *values):
        return self.deviate_linearity(self.hash_combine(self.xor_combine(*values))) * self.sum_fractional(
            self.fractional_result)
