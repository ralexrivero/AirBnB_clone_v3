#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class Pep8Docs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_console(self):
        """Test that console.py for PEP8"""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style and warnings to be fixed.")

    def test_pep8_test_console(self):
        """Test that (this) tests/test_console.py for PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style and warnings to be fixed.")

    def test_console_module_docstring(self):
        """Test docstrings in console.py"""
        self.assertIsNot(console.__doc__, None,
                         "Docstring needs to be included in console.py")
        self.assertTrue(len(console.__doc__) >= 1,
                        "Docstring needs to be included in console.py")

    def test_HBNBCommand_class_docstring(self):
        """HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "Docstring needs to be included in HBNBCommand")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "Docstring needs to be included in HBNBCommand")
