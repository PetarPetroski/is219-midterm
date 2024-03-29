from app.commands import Command
import logging
import pandas
class Mean(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) < 2:
            logging.error("Invalid input: Please provide at least two numbers.")
            return
        
        numbers = [int(num) for num in numbers]
        mean = sum(numbers) / len(numbers)
        
        logging.info(f"The mean is: {mean}")
        return result
