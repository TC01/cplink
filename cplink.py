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
import shutil
import sys

def cplink(directory, verbose=False):
	try:
		source = os.readlink(directory)
		if verbose:
			print "Read link " + directory + " -> " + source
		os.remove(directory)
		if verbose:
			print "Deleted link " + directory
		shutil.copytree(source, directory)
		if verbose:
			print "Recursively copying " + source + " to " + directory
	except:
		# Because isn't this everyone's favorite error message?
		print "Error: no such file or directory."

def main():
	"""Main function of script."""
	parser = argparse.ArgumentParser(description="Tool to unlink two directories and make a unique copy in place of the link.")
	parser.add_argument("directory", metavar="DIR", type=str, help="The directory to unlink and replace.")
	parser.add_argument("-r", "--recursive", action="store_true", dest="recursive", help="Recursively fix all links in DIR.")
	parser.add_argument("-v", "--verbose", action="store_true", dest="verbose", help="Enable verbose command line output.")
	args = parser.parse_args()

	# Do some sanitation
	# I know that "it's better to ask forgiveness than permission", but meh
	directory = os.path.abspath(args.directory)
	if not os.path.exists(directory):
		print "Error: no such directory."

	cplink(directory, args.verbose)

if __name__ == '__main__':
	main()