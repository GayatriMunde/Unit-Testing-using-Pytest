class Odometer:
    def __init__(self, length_of_odometer = 0):
        self.length_of_odometer = length_of_odometer
        self.valid_readings = []
        self.num_of_readings = 0

    def is_ascending(self, reading : int) -> bool:
        sort_reading = list(map(str , sorted(list(str(reading)))))
        return(reading == int(''.join(sort_reading)) and len(set(sort_reading)) == len(sort_reading))

    def generate_readings(self):
        start = pow(10, self.length_of_odometer - 1)
        end = pow(10, self.length_of_odometer)
        for value in range(start, end):
            if self.is_ascending(value):
                self.valid_readings.append(value)
        self.num_of_readings = len(self.valid_readings)
        return(self.valid_readings)

    def next_reading(self, current_reading : int) -> int:
        self.generate_readings()
        return(self.valid_readings[(self.valid_readings.index(current_reading) + 1) % self.num_of_readings])

    def previous_reading(self, current_reading : int) -> int:
        self.generate_readings()
        return(self.valid_readings[(self.valid_readings.index(current_reading) - 1) % self.num_of_readings])

