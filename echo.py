#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "jayaimzzz"


import sys
import argparse


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("text", help="text to be manipulated")
    parser.add_argument("-u", "--upper", help="convert text to uppercase", action="store_true")
    parser.add_argument("-l","--lower", help="convert text to lowercase", action="store_true")
    parser.add_argument("-t","--title", help="convert text to titlecase", action="store_true")
    return parser



def main(args):
    parser = create_parser()
    args = parser.parse_args(args)
    # print args
    result = args.text
    if args.upper:
        result = result.upper()
    if args.lower:
        result = result.lower()
    if args.title:
        result = result.title()
    return result

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
    
