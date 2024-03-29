from unittest import TestCase
from unittest.mock import patch
from app.plugins.add import Add
from app.plugins.subtract import Subtract
from app.plugins.multiply import Multiply
from app.plugins.divide import Divide
from app.plugins.exponent import Exponent
from app.plugins.factorial import Factorial
from app.plugins.mean import Mean
from app.plugins.mode import Mode
from app.plugins.exit import ExitCommand

class TestAdd(TestCase):
    def setUp(self):
        self.add_command = Add()

    def test_execute_with_valid_args(self):
        args = "2 3"
        expected_result = 5
        with patch('logging.info') as mock_logging_info:
            result = self.add_command.execute(args)
            mock_logging_info.assert_called_once_with("The sum is: 5")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "2"
        with patch('logging.error') as mock_logging_error:
            result = self.add_command.execute(args)
            mock_logging_error.assert_called_once_with('At least 2 numbers are required.')
            self.assertIsNone(result)

class TestSubtract(TestCase):
    def setUp(self):
        self.subtract_command = Subtract()

    def test_execute_with_valid_args(self):
        args = "5 2"
        expected_result = 3
        with patch('logging.info') as mock_logging_info:
            result = self.subtract_command.execute(args)
            mock_logging_info.assert_called_once_with("The difference is: 3")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "5"
        with patch('logging.error') as mock_logging_error:
            result = self.subtract_command.execute(args)
            mock_logging_error.assert_called_once_with("Please provide at least two numbers.")
            self.assertIsNone(result)

class TestMultiply(TestCase):
    def setUp(self):
        self.multiply_command = Multiply()

    def test_execute_with_valid_args(self):
        args = "2 3"
        expected_result = 6
        with patch('logging.info') as mock_logging_info:
            result = self.multiply_command.execute(args)
            mock_logging_info.assert_called_once_with("The product is: 6")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "2"
        with patch('logging.error') as mock_logging_error:
            result = self.multiply_command.execute(args)
            mock_logging_error.assert_called_once_with("Please provide at least two numbers.")
            self.assertIsNone(result)

class TestDivide(TestCase):
    def setUp(self):
        self.divide_command = Divide()

    def test_execute_with_valid_args(self):
        args = "6 3"
        expected_result = 2.0
        with patch('logging.info') as mock_logging_info:
            result = self.divide_command.execute(args)
            mock_logging_info.assert_called_once_with("The quotient is: 2.0")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "6"
        with patch('logging.error') as mock_logging_error:
            result = self.divide_command.execute(args)
            mock_logging_error.assert_called_once_with("Please provide at least two numbers.")
            self.assertIsNone(result)

class TestExponent(TestCase):
    def setUp(self):
        self.exponent_command = Exponent()

    def test_execute_with_valid_args(self):
        args = "2 3"
        expected_result = 8
        with patch('logging.info') as mock_logging_info:
            result = self.exponent_command.execute(args)
            mock_logging_info.assert_called_once_with("The result is: 8")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "2"
        with patch('logging.error') as mock_logging_error:
            result = self.exponent_command.execute(args)
            mock_logging_error.assert_called_once_with('Invalid input: Please provide exactly two numbers.')
            self.assertIsNone(result)

class TestFactorial(TestCase):
    def setUp(self):
        self.factorial_command = Factorial()

    def test_execute_with_valid_args(self):
        args = "5"
        expected_result = 120
        with patch('logging.info') as mock_logging_info:
            result = self.factorial_command.execute(args)
            mock_logging_info.assert_called_once_with('The factorial of 5 is: 120')
            self.assertEqual(result, expected_result)

class TestMean(TestCase):
    def setUp(self):
        self.mean_command = Mean()

    def test_execute_with_valid_args(self):
        args = "1 2 3 4 5"
        expected_result = 3
        with patch('logging.info') as mock_logging_info:
            result = self.mean_command.execute(args)
            mock_logging_info.assert_called_once_with("The mean is: 3.0")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "1"
        with patch('logging.error') as mock_logging_error:
            result = self.mean_command.execute(args)
            mock_logging_error.assert_called_once_with("Invalid input: Please provide at least two numbers.")
            self.assertIsNone(result)

class TestMode(TestCase):
    def setUp(self):
        self.mode_command = Mode()

    def test_execute_with_valid_args(self):
        args = "1 2 2 3 4 5"
        expected_result = [2]
        with patch('logging.info') as mock_logging_info:
            result = self.mode_command.execute(args)
            mock_logging_info.assert_called_once_with("The modes are: 2")
            self.assertEqual(result, expected_result)

    def test_execute_with_insufficient_args(self):
        args = "1"
        with patch('logging.error') as mock_logging_error:
            result = self.mode_command.execute(args)
            mock_logging_error.assert_called_once_with('Invalid input: Please provide at least two numbers.')
            self.assertIsNone(result)

class TestExit(TestCase):
    def setUp(self):
        self.exit_command = ExitCommand()

    def test_execute(self):
        with patch('logging.info') as mock_logging_info:
            try:
                result = self.exit_command.execute()
            except SystemExit as e:
                result = str(e)
            mock_logging_info.assert_called_once_with("Exiting...")
            self.assertEqual(result, "Exiting...")

if __name__ == '__main__':
    unittest.main()