from app.commands import Command
import logging
import statistics

class Mode(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) < 2:
            logging.error("Invalid input: Please provide at least two numbers.")
            return
        
        try:
            numbers = list(map(int, numbers))
            modes = statistics.multimode(numbers)
            
            if len(modes) == 0:
                logging.info("No mode found.")
            else:
                logging.info("The modes are: " + ", ".join(map(str, modes)))
        except statistics.StatisticsError:
            logging.info("No mode found.")
            