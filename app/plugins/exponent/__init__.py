from app.commands import Command
import logging

class Exponent(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) != 2:
            logging.error("Invalid input: Please provide exactly two numbers.")
            return
        
        result = int(numbers[0]) ** int(numbers[1])
        logging.info(f"The result is: {result}")
        return result