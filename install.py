#!/usr/bin/env python3

"""
0000  00000 00000 00000 0     00000
00  0 00      0   0     0       0  
00000 00000   0   0     0       0
00       00   0   0     0       0
00    00000 00000 00000 00000 00000
(psicli)
- INSTALLER EDITION -

v2.1.4

A blob that installs psicli (the cli-wrapper
for psilib), and psilib.

Copyright (c) 2019 Ong Yong Xin
Open-sourced under the MIT License.

Source:
https://github.com/sn3ksoftware/psicli
"""

# Import needed modules.
import os
import sys
import shutil
import zipfile
import platform
import requests

# Get options from sys.argv


def chkarg1():
	try:
		arg1 = sys.argv[1]
	except IndexError:
		return False
	else:
		return True
		
# Check install platform


def chkplat():
	if platform.machine().startswith("iP"):
		# iOS
		try:
			import objc_util
		except ImportError:
			# Running on Libterm, return path to scripts and psicfg.
			inslist = ["~/Library/bin",
			"~/Documents/.psicfg",
			"Libterm"]
			return inslist
		else:
			# Running on Pythonista, check if StaSh is installed.
			try:
				import stash
			except ImportError:
				print("\nE: StaSh is not installed. Please install StaSh first"
				"with [import requests as r; exec(r.get('https://bit.ly/"
				"get-stash').text)].")
				exit()
			else:
				print("\nInstaller is running on Pythonista, "
				"StaSh is installed.")
				inslist = ["~/Documents/bin",
				"~/Documents/.psicfg",
				"Pythonista"]
				return inslist
	else:
		# Not running on iOS: Platform not supported.
		raise NotImplementedError("\nE: Your platform is not supported.")
		
# Declare needed vars.
paths = chkplat()
home = os.path.expanduser("~/Documents/")
script_p = os.path.expanduser(paths[0])
psicfg_p = os.path.expanduser(paths[1])
tmp = psicfg_p + "/tmp/"
site_packages = next(p for p in sys.path if 'site-packages' in p)
plat = paths[2]
	
# Define extractfile function
# Copied from zip2 command


def extractfile(filepath, dest):
	# Parse filepath
	filepath_p = os.path.expanduser(filepath)
	dest_p = os.path.expanduser(dest)
	print("\nExtracting...")
	with zipfile.ZipFile(filepath_p, 'r') as zip:
		try:
			zip.extractall(path=dest_p)
		except zipfile.BadZipfile:
			print("\nE: Zip file is bad (corrupted?)\nAbort.")
		else:
			print("\nSucessfully extracted.")
			
# Define download function.


def dl(url, path=""):
	# Parse out path to be usable
	path_p = os.path.expanduser(path)
	# Split url and get filename
	filename = url.split("/")[-1]
	file = requests.get(url).content
	with open(path_p + filename, "wb") as f:
		f.write(file)
		
# Download psicli from repo and unzip to script folder.


def getpsi():
	resource_path = home + "resources.zip"
	print("\nStarting install of PSI...")
	
	# Download resources file and extract to
	# .psicfg
	dl("https://raw.githubusercontent.com/sn3ksoftware/psilib/master/resources.zip", path=home)
	try:
		os.mkdir(home + ".psicfg")
	except OSError:
		shutil.rmtree(home + ".psicfg")
		os.mkdir(home + ".psicfg")
	
	extractfile(resource_path, home + ".psicfg")
	
	print("\nGetting psicli/psilib...")
	
	# Download psicli and psilib
	dl("https://raw.githubusercontent.com/sn3ksoftware/psidex/master/packages/rolling/psicli.zip", path=tmp)
	dl("https://raw.githubusercontent.com/sn3ksoftware/psidex/master/packages/rolling/psilib.zip", path=tmp)
	
	try:
		os.mkdir(site_packages + "/psilib")
	except OSError:
		print("\nW: psilib already exists.\nReplacing...")
		shutil.rmtree(site_packages + "/psilib")
		os.mkdir(site_packages + "/psilib")
	else:
		pass
	
	# Extract psilib to site-packages, and
	# move psicli.py to script path.
	# If user specifes [-m] option, install
	# psilib module only.
	if chkarg1():
		if sys.argv[1] == "-m":
			extractfile(tmp + "psilib.zip", site_packages + "/psilib/")
			print("\nInstalled psilib only.")
	else:
		extractfile(tmp + "psilib.zip", site_packages + "/psilib/")
		extractfile(tmp + "psicli.zip", script_p)
		# Clean up tmp folder and delete
		# resources.zip
		for file in os.listdir(tmp):
			tmpfile = os.path.join(tmp, file)
			os.remove(tmpfile)
		os.remove(resource_path)
		print("\nInstalled both psicli and psilib.")
			
if __name__ == '__main__':
	getpsi()
