import psutil
import random


class Network:
    @staticmethod
    def get_network_io_counters():
        return psutil.net_io_counters(pernic=True)

    def return_value(self):
        network_counters = self.get_network_io_counters()

        total_bytes_sent = sum(interface.bytes_sent for interface in network_counters.values())
        total_bytes_recv = sum(interface.bytes_recv for interface in network_counters.values())

        return total_bytes_sent + total_bytes_recv * random.randint(1, 100)
