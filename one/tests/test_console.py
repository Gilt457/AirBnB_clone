#!/usr/bin/python3
"""Module for testing the HBNBCommand Class."""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test the HBNBCommand Console."""

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
        expected = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        actual = output.getvalue()
        self.assertEqual(expected, actual)

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("quit")
        # simulate what happens when someone types `quit`
        actual = output.getvalue()
        self.assertEqual("", actual)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("quit garbage")
        # simulate when user types `quit anything`
        actual = output.getvalue()
        self.assertEqual("", actual)

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
        # simulate what happens when user types `quit`
        actual = output.getvalue()
        self.assertEqual("\n", actual)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("EOF garbage")
        # simulate when user types `EOF anything`
        actual = output.getvalue()
        self.assertEqual("\n", actual)

    def test_emptyline(self):
        """Test the emptyline command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("\n")
        # simulate what happens when user doesn't type anything
        actual = output.getvalue()
        self.assertEqual("", actual)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("                     \n")
        # simulate when user types lots of whitespaces & enter
        actual = output.getvalue()
        self.assertEqual("", actual)

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all")

    # Test cases for count
    # Test cases for show
    # Test cases for create
    # Test cases for update
    # Test cases for destroy


if __name__ == "__main__":
    unittest.main()
