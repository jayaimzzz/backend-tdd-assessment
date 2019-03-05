#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here

class TestEcho(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()
        self.assertEquals(stdout, usage)
        
    def test_upper(self):
        args = ["Hello", "-u"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        args = ["Hello", "--upper"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.upper)
        self.assertEquals(echo.main(args), "HELLO")
        
    def test_lower(self):
        args = ["Hello", "-l"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)
        args = ["Hello", "--lower"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.lower)
        self.assertEquals(echo.main(args), "hello")
    
    def test_title(self):
        args = ["hello", "-t"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)
        args = ["hello", "--title"]
        parser = echo.create_parser()
        namespace = parser.parse_args(args)
        self.assertTrue(namespace.title)
        self.assertEquals(echo.main(args), "Hello")

    def test_all_options(self):
        args = ["hello", "-utl"]
        self.assertEquals(echo.main(args), "Hello")

    def test_no_args(self):
        args = ["hElLo"]
        self.assertEquals(echo.main(args),"hElLo")

if __name__ == '__main__':
    unittest.main()
