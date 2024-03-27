from app.commands import Command
import logging

class Add(Command):
    def execute(self, args):
        numbers = args.split()
        result = sum(map(int, numbers))
        print(f"The sum is: {result}")
        logging.info(f"The sum is: {result}")