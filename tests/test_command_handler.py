"""
This module contains unit tests for the CommandHandler class.
"""

import unittest
from unittest.mock import patch, Mock
from app.commands import CommandHandler, Command  # replace 'app.commands' with the actual module name

class TestCommandHandler(unittest.TestCase):
    """
    This class contains unit tests for the CommandHandler class.
    """

    def setUp(self):
        """
        This method sets up the test environment for each test.
        """
        self.command_handler = CommandHandler()

    def test_register_command(self):
        """
        This method tests the register_command method with valid arguments.
        """
        command = Mock(spec=Command)
        self.command_handler.register_command('test', command)
        self.assertIn('test', self.command_handler.commands)

    @patch('builtins.print')
    def test_list_commands(self, mock_print):
        """
        This method tests the list_commands method with valid arguments.
        """
        command = Mock(spec=Command)
        self.command_handler.register_command('test', command)
        self.command_handler.list_commands()
        mock_print.assert_any_call('Available commands:')
        mock_print.assert_any_call('test')

    @patch('pandas.DataFrame.to_csv')
    def test_save_history(self, mock_to_csv):
        """
        This method tests the save_history method with valid arguments.
        """
        self.command_handler.save_history()
        mock_to_csv.assert_called_once_with('history.csv', index=False)

    @patch('pandas.read_csv')
    def test_load_history(self, mock_read_csv):
        """
        This method tests the load_history method with valid arguments.
        """
        self.command_handler.load_history()
        mock_read_csv.assert_called_once_with('history.csv')

    def test_clear_history(self):
        """
        This method tests the clear_history method with valid arguments.
        """
        self.command_handler.clear_history()
        self.assertTrue(self.command_handler.history.empty)

    @patch('app.commands.logging.info')
    @patch('app.commands.CommandHandler.list_commands')
    def test_execute_command_menu(self, mock_list_commands, mock_logging_info):
        """
        This method tests the execute_command method with 'menu' argument.
        """
        self.command_handler.execute_command('menu')
        mock_list_commands.assert_called_once()
        mock_logging_info.assert_called_once_with("Menu command executed")

    @patch('app.commands.logging.info')
    @patch('app.commands.logging.warning')
    @patch('builtins.print')
    def test_execute_command_unknown(self, mock_print, mock_logging_warning, mock_logging_info):
        """
        This method tests the execute_command method with an unknown command.
        """
        self.command_handler.execute_command('unknown')
        mock_print.assert_called_once_with("No such command: unknown")
        mock_logging_warning.assert_called_once_with("No such command: unknown")


if __name__ == '__main__':
    unittest.main()
