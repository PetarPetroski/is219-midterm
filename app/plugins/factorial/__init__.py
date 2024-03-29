from app.commands import Command
import logging
import math

class Factorial(Command):
    def execute(self, args):
        if len(args) != 1:
            logging.warning("Only one number should be provided.")
            return
        
        number = int(args[0])
        
        result = math.factorial(number)
        logging.info(f"The factorial of {number} is: {result}")
        return result
