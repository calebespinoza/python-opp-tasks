from datetime import datetime
import time

class Timer:

    __FMT = '%H:%M:%S'

    def time_delta(self, time_in, time_exit):
        delta = datetime.strptime(time_exit, self.__FMT) - datetime.strptime(time_in, self.__FMT)
        return delta.total_seconds() / 60
    