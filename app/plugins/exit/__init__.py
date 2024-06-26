import sys
import logging
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        logging.info("Exiting...")
        sys.exit("Exiting...")
        return "Exiting..."