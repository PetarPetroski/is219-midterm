from app.commands import Command
import logging
import statistics

class Mode(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) < 2:
            print("Please provide at least two numbers.")
            logging.error("Invalid input: Please provide at least two numbers.")
            return
        
        try:
            numbers = list(map(int, numbers))
            modes = statistics.multimode(numbers)
            
            if len(modes) == 0:
                print("No mode found.")
                logging.info("No mode found.")
            else:
                print("The modes are:", ", ".join(map(str, modes)))
                logging.info("The modes are: " + ", ".join(map(str, modes)))
        except statistics.StatisticsError:
            print("No mode found.")
            logging.info("No mode found.")