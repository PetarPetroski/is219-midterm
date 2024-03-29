from app.commands import Command
import logging

class Multiply(Command):
    
    def execute(self, args):

        numbers = args.split()
        if len(numbers) < 2:
            logging.error("Please provide at least two numbers.")
            return
        result = 1
        for num in numbers:
            result *= int(num)
        logging.info(f"The product is: {result}")
        return result