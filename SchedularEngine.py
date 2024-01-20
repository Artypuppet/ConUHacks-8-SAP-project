import Scheduler
import sys
import Logger

def main():

    #Validate argument list
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
    
    #Instantiate schedular
    scheduler = Scheduler(sys.argv[1])

    #Attach observers to subject
    scheduler.attach(Logger())

    scheduler.attach() # Attach statistics tracker





if __name__ == "__main__":
    main()