import time
import os

class Program: 
    @staticmethod
    def Sleep(seconds):
        time.sleep(seconds)
    
    @staticmethod
    def Exit(value):
        os._exit(value)
    
    @staticmethod
    def SetDirectoryToCurrent():
        os.chdir(os.getcwd())
    