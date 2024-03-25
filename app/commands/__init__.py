from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_input):
        command_name, *args = command_input.split()
        args = ' '.join(args)
        if command_name == "menu":
            self.list_commands()
        elif command_name in self.commands:
            self.commands[command_name].execute(args)
        else:
            print(f"No such command: {command_name}")

    def list_commands(self):
        print("Available commands:")
        for command_name in self.commands:
            print(command_name)