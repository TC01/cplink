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
	current = os.getcwd()

	source = os.readlink(directory)

	# We need to get ../ from the director, then chdir there, then abspath.
	relative = directory[:directory.rfind("/") + 1]
	os.chdir(relative)

	source = os.path.abspath(source)
	if verbose:
		print("Read link " + directory + " -> " + source)

	os.remove(directory)
	if verbose:
		print("Deleted link " + directory)

	shutil.copytree(source, directory)
	if verbose:
		print("Recursively copying " + source + " to " + directory)

	os.chdir(current)

def cplink_recursive(directory, verbose=False):
	"""	Implement recursive logic; cplink function does not recurse."""
	for path, dirs, files in os.walk(directory):
		for newdir in dirs:
			newdir = os.path.join(path, newdir)
			if os.path.islink(newdir):
				cplink(newdir, verbose)

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
		print("Error: no such directory.")

	if os.path.islink(directory):
		link = os.readlink(directory)
		try:
			cplink(directory, args.verbose)
		except:
			# Because isn't this everyone's favorite error message?
			print("Error: no such file or directory.")
	elif args.recursive:
		try:
			cplink_recursive(newdir, args.verbose)
		except:
			print("Error: no such file or directory.")
	else:
		print("Error: please run with -r (--recursive) for recursive parsing of links.")

if __name__ == '__main__':
	main()
