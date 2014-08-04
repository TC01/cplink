#!/usr/bin/env python

"""
cplink

Basically, it does what it says on the tin. Example:

a ==> b

cplink b:
rm b
cp -r a/ b/

So, it unlinks two things but replaces the link with the original source.
"""

import argparse
import os
import sys

def main():
	"""Main function of script."""
	

if __name__ == '__main__':
	main()