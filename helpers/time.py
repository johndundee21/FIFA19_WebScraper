import time
import datetime as Date

class Time:
    @staticmethod
    def Stamp():
        TimeStamp = time.time()
        return Date.datetime.fromtimestamp(TimeStamp).strftime('%d-%m-%Y %H:%M:%S')

        