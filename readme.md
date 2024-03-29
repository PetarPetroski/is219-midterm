# README.md

## Setup Instructions

1. Clone the repository
2. Install the required dependencies
3. Run the application

## Usage Examples

To execute a command, use the `execute_command` method of the `CommandHandler` class. For example:

```python
command_handler = CommandHandler()
command_handler.execute_command("command_name")
```

## Architectural Decisions

### Design Patterns

The Command design pattern is used in this application. This pattern encapsulates a request as an object, thereby allowing users to parameterize clients with queues, requests, and operations.

See the implementation [here](./app/commands.py).

### Environment Variables

Environment variables are used to configure the application. They are loaded when the application starts.

See the implementation [here](./__init__.py#L19-L24).

### Logging

Logging is configured at the start of the application. If a logging configuration file exists, it is used; otherwise, a basic configuration is used.

See the implementation [here](./__init__.py#L14-L18).

### Exception Handling

The application uses the "Easier to Ask for Forgiveness than Permission" (EAFP) style of exception handling. This is evident when loading plugins, where an attempt is made to import the plugin module, and if it fails, an error is logged.

See the implementation [here](./__init__.py#L39-L47).

## Video Demonstration

A video demonstration of the application can be found [here](#).

## Additional Code

The additional code provided includes the `Command` abstract base class and the `CommandHandler` class. The `CommandHandler` class maintains a history of executed commands and provides methods for executing commands, listing available commands, displaying command history, and saving/loading/clearing command history.

See the implementation [here](./app/commands.py).