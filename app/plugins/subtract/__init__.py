from app.commands import Command
import logging

class Subtract(Command):
    
    def execute(self, args):
        numbers = args.split()
        if len(numbers) < 2:
            print("Please provide at least two numbers.")
            logging.error("Please provide at least two numbers.")
            return
        result = int(numbers[0]) - sum(map(int, numbers[1:]))
        print(f"The difference is: {result}")
        logging.info(f"The difference is: {result}")
