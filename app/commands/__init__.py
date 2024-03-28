import pandas as pd
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.history = pd.DataFrame(columns=['command', 'args', 'result'])

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_input):
        command_name, *args = command_input.split()
        args = ' '.join(args)
        if command_name == "menu":
            self.list_commands()
        elif command_name == "history":
            self.show_history()
        elif command_name == "save":
            self.save_history()
        elif command_name == "load":
            self.load_history()
        elif command_name == "clear":
            self.clear_history()
        elif command_name in self.commands:
            result = self.commands[command_name].execute(args)
            new_row = pd.DataFrame({'command': [command_name], 'args': [args], 'result': [result]})
            self.history = self.history._append(new_row, ignore_index=True)        
        else:
            print(f"No such command: {command_name}")

    def list_commands(self):
        print("Available commands:")
        for command_name in self.commands:
            print(command_name)

    def show_history(self):
        print(self.history)

    def save_history(self):
        self.history.to_csv('history.csv', index=False)

    def load_history(self):
        self.history = pd.read_csv('history.csv')

    def clear_history(self):
        self.history = pd.DataFrame(columns=['command', 'args', 'result'])