from app.commands import Command
import logging

class Divide(Command):
    
    def execute(self, args):
        numbers = args.split()
        if len(numbers) < 2:
            print("Please provide at least two numbers.")
            logging.error("Please provide at least two numbers.")
            return
        result = int(numbers[0])
        for num in numbers[1:]:
            if int(num) == 0:
                print("Cannot divide by zero.")
                logging.error("Cannot divide by zero.")
                return
            result /= int(num)
        print(f"The quotient is: {result}")
        logging.info(f"The quotient is: {result}")
