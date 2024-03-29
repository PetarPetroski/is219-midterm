# Calculator Project

This project is a Python calculator application that provides basic and statistical operations.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone git@github.com:PetarPetroski/is219-midterm.git
   cd is219-midterm
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Activate the virtual environment (Linux/Mac)
   venv\Scripts\activate  # Activate the virtual environment (Windows)
   ```

3. **Install the required dependencies from `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python3 main.py
   ```

## Usage Examples

To execute a command, type the command from the list and number(s) separated by spaces

- `add [num1] [num2]`: This command adds two numbers. Example: `add 1 2` will return `3`.

- `mode [num1] [num2] [num3] ...`: This command calculates the mode of a list of numbers. Example: `mode 1 1 2 3 4 5` will return `1`.

- `factorial [num]`: This command calculates the factorial of a number. Example: `factorial 5` will return `120`.

- `mean [num1] [num2] [num3] ...`: This command calculates the mean of a list of numbers. Example: `mean 1 2 3 4 5` will return `3`.

- `subtract [num1] [num2]`: This command subtracts the second number from the first. Example: `subtract 5 2` will return `3`.

- `multiply [num1] [num2]`: This command multiplies two numbers. Example: `multiply 3 4` will return `12`.

- `divide [num1] [num2]`: This command divides the first number by the second. Example: `divide 10 2` will return `5`. Note: The second number must not be `0`.

- `exponent [num1] [num2]`: This command raises the first number to the power of the second. Example: `exponent 2 3` will return `8`.


Remember to separate each argument with a space. For commands that take a list of numbers, you can provide as many numbers as you want.
## History Functionality

The application maintains a history of all the commands that have been executed. This is useful for tracking what operations have been performed and in what order. Here are some commands related to the history functionality:

- `history`: This command displays the history of all the commands that have been executed. Each entry in the history includes the command that was executed, the arguments it was given, and the result it produced.

- `save`: This command saves the current command history to a file. This allows you to keep a permanent record of the commands that have been executed.

- `load`: This command loads a previously saved command history from a file. This can be useful if you want to review or repeat a sequence of commands.

- `clear`: This command clears the current command history. Use this if you want to start a new sequence of commands without the old ones being in the way.

Remember, the history functionality is not just for keeping track of what you've done. It's also a powerful tool for understanding how your commands have affected the state of the system.

## Design Patterns

### Singleton
The Singleton design pattern is used to ensure a class has only one instance, and provide a global point of access to it. This is particularly useful when a single shared resource, like a database connection or a configuration setting, needs to be managed.

In this application, the `App` class could be considered as a Singleton if it's ensured that only one instance of `App` is created throughout the application. However, the code does not enforce this, so it's not a strict Singleton.

See the implementation in this code:

```python
if __name__ == "__main__":
    app = App()
    app.start()
```

### Command
The Command design pattern is used to encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

In this application, the `App` class registers commands with a `CommandHandler` in the `register_plugin_commands` method. Each command is an instance of a subclass of `Command`. The `CommandHandler` is then responsible for executing these commands. The specific command to execute is determined at runtime based on user input.

See the implementation in this code:

```python
def register_plugin_commands(self, plugin_module, plugin_name):
    for item_name in dir(plugin_module):
        item = getattr(plugin_module, item_name)
        if isinstance(item, type) and issubclass(item, Command) and item is not Command:
            # Command names are now explicitly set to the plugin's folder name
            self.command_handler.register_command(plugin_name, item())
            logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")
```

### Factory Method
The Factory Method design pattern is used to provide an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This provides a high level of flexibility for the code.

In this application, the `CommandHandler` class is part of a Factory Method pattern. It's responsible for creating instances of `Command` subclasses based on the command name input. The specific `Command` subclass to instantiate is determined at runtime based on the command name.

See the implementation in this code:

```python
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_input):
        command_name, *args = command_input.split()
        args = ' '.join(args)
        if command_name in self.commands:
            result = self.commands[command_name].execute(args)
            logging.info(f"Command '{command_name}' executed with args '{args}'")
        else:
            print(f"No such command: {command_name}")
            logging.warning(f"No such command: {command_name}")
```

## Environment Variables

Environment variables are used to configure the application. They are loaded when the application starts.

See the implementation [here](./logging.conf).

## Logging

Logging is configured at the start of the application. If a logging configuration file exists, it is used; otherwise, a basic configuration is used.

See the implementation [here](./app/__init__.py).

## Exception Handling

The application uses the "Easier to Ask for Forgiveness than Permission" (EAFP) style of exception handling. This is evident when loading plugins, where an attempt is made to import the plugin module, and if it fails, an error is logged.

See the implementation [here](./app/__init__.py).

## Video Demonstration

A video demonstration of the application can be found [here](https://youtu.be/MZ5tDR0BoAc).
