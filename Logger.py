import Observer
import sys

class Logger(Observer):

    def __init__(self):
        try:
            self.file = open("loggerfile.txt", "a")
        except:
            print("File could not open.", file=sys.stderr)
            print("Exiting program...")
            sys.exit(1)
    
    def update(self,statement: str):
        try:
            self.file.write(statement)
        except:
            print("Could not write to loggerfile.txt", file=sys.stderr)