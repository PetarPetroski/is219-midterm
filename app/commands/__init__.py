import pandas as pd
import logging
from abc import ABC, abstractmethod
import logging
import logging.config

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.history = pd.DataFrame(columns=['command', 'args'])

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_input):
        command_name, *args = command_input.split()
        args = ' '.join(args)
        if command_name == "menu":
            self.list_commands()
            logging.info("Menu command executed")
        elif command_name == "history":
            self.show_history()
            logging.info("History command executed")
        elif command_name == "save":
            self.save_history()
            logging.info("Save command executed")
        elif command_name == "load":
            self.load_history()
            logging.info("Load command executed")
        elif command_name == "clear":
            self.clear_history()
            logging.info("Clear command executed")
        elif command_name in self.commands:
            result = self.commands[command_name].execute(args)
            new_row = pd.DataFrame({'command': [command_name], 'args': [args]})
            self.history = self.history._append(new_row, ignore_index=True)
            logging.info(f"Command '{command_name}' executed with args '{args}'")
        else:
            print(f"No such command: {command_name}")
            logging.warning(f"No such command: {command_name}")

    def list_commands(self):
        print("Available commands:")
        for command_name in self.commands:
            print(command_name)

    def show_history(self):
        for index, row in self.history.iterrows():
            command = row['command']
            args = row['args']
            if command in self.commands:
                result = self.commands[command].execute(args)
                print(f"Command: {command}, Args: {args}, Result: {result}")
            else:
                print(f"Command: {command}, Args: {args}, Result: Command not found")
        logging.info("History displayed")

    def save_history(self):
        self.history.to_csv('history.csv', index=False)
        logging.info("History saved to file")

    def load_history(self):
        self.history = pd.read_csv('history.csv')
        logging.info("History loaded from file")

    def clear_history(self):
        self.history = pd.DataFrame(columns=['command', 'args'])
        logging.info("History cleared")