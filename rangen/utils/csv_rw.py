import csv

class CSVManager:
    def __init__(self, csv_file_location):
        self.csv_file_location = csv_file_location

    def save_data(self, data):
        with open(self.csv_file_location, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for value in data:
                csv_writer.writerow([str(value)])

    def fetch_data(self):
        read_data = []
        with open(self.csv_file_location, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                read_data.append(int(row[0]))
        return read_data
