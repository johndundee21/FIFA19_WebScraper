import os
from helpers.program import Program

class File: 
    @staticmethod
    def Exists(filename):
        return os.path.isfile(filename)
    
    @staticmethod
    def Error():
        print("Error: File does not exist!")
        Program.Sleep(2)
        Program.Exit(0)
