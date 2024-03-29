# README.md

## Setup Instructions

1. Ensure that you have Python 3.6 or later installed on your system. You can verify this by running `python --version` in your terminal. If you don't have Python installed, you can download it from the [official website](https://www.python.org/downloads/).

2. Install the required Python packages. This project requires the `pandas` package. You can install it using pip:

```bash
pip install pandas
```

3. Clone the repository to your local machine and navigate to the project directory.

## Usage Examples

This project is designed to handle commands. Here's an example of how to use it:

```python
handler = CommandHandler()
handler.register_command("example", ExampleCommand())
handler.execute_command("example arg1 arg2")
```

## Architectural Decisions

### Command Pattern

The command pattern is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request's execution, and support undoable operations.

In this project, the `Command` class is an abstract base class that represents a command. Concrete commands should inherit from this class and implement the `execute` method.

The `CommandHandler` class is responsible for registering and executing commands. It maintains a history of executed commands, which can be saved to and loaded from a CSV file.

### Logging Strategy

The project uses Python's built-in `logging` module to log events. The logging level is set to `INFO`, so all `INFO`, `WARNING`, `ERROR`, and `CRITICAL` messages will be logged.

The `logging.config` module is also imported, which allows for flexible configuration of logging. However, in the current implementation, the default configuration is used.

When a command is executed, an `INFO` message is logged. If an unknown command is attempted, a `WARNING` message is logged.

## Impact of Design Patterns and Logging Strategy

The command pattern provides several benefits:

- Decouples the sender and receiver of a request.
- Allows for the parameterization of commands, making it easy to add new commands.
- Supports undoable operations, although this feature is not implemented in this project.

The logging strategy provides a way to track the flow of execution and debug issues. By logging an `INFO` message every time a command is executed, it's easy to see the sequence of commands that led to a particular state. The `WARNING` messages provide a way to identify attempts to execute unknown commands.