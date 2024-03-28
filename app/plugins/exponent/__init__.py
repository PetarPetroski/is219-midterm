from app.commands import Command
import logging

class Exponent(Command):
    def execute(self, args):
        numbers = args.split()
        
        if len(numbers) != 2:
            print("Please provide exactly two numbers.")
            logging.error("Invalid input: Please provide exactly two numbers.")
            return
        
        result = int(numbers[0]) ** int(numbers[1])
        print(f"The result is: {result}")
        logging.info(f"The result is: {result}")