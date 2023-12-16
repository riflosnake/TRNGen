import random

import psutil
import time

class Disk:
    def __init__(self, interval=1):
        self.interval = interval
    @staticmethod
    def get_disk_io_counters():
        return psutil.disk_io_counters(perdisk=True)

    def return_value(self):
        disk_counters_before = self.get_disk_io_counters()
        time.sleep(self.interval)
        disk_counters_after = self.get_disk_io_counters()

        io_counters_diff = {}
        for disk, before in disk_counters_before.items():
            after = disk_counters_after.get(disk, None)
            if after:
                io_counters_diff[disk] = {
                    'read_bytes': after.read_bytes - before.read_bytes,
                    'write_bytes': after.write_bytes - before.write_bytes,
                }

        read_write_bytes_sum_per_disk = []
        for disk, counters in io_counters_diff.items():
            read_write_bytes_sum_per_disk.append(counters["read_bytes"] + counters["write_bytes"])

        return read_write_bytes_sum_per_disk[random.randint(0, len(read_write_bytes_sum_per_disk) - 1)]

