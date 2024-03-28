from app.commands import Command
import logging

class Mean(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) < 2:
            print("Please provide at least two numbers.")
            logging.error("Invalid input: Please provide at least two numbers.")
            return
        
        numbers = [int(num) for num in numbers]
        mean = sum(numbers) / len(numbers)
        
        print(f"The mean is: {mean}")
        logging.info(f"The mean is: {mean}")
