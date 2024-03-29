from app.commands import Command
import logging

class Add(Command):
    def execute(self, args):
        numbers = args.split()
        if len(numbers) < 2:
            logging.error("At least 2 numbers are required.")
            return None
        result = sum(map(int, numbers))
        logging.info(f"The sum is: {result}")
        return result