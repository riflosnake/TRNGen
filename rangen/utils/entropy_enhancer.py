import hashlib


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
        return sum([int(fraction * 10**len(str(fraction).split('.')[1])) if fraction != 0 else 0 for fraction in fractions])

    def extract(self, *values):
        return self.hash_combine(self.xor_combine(*values)) * self.sum_fractional(self.fractional_result)
