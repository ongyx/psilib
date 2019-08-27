#!/usr/bin/env python3

"""
0000  00000 00000 0   0   0   00  0
00  0 00      0   00 00  0 0  00  0
00000 00000   0   0 0 0 00000 0 0 0
00       00   0   0   0 0   0 0  00
00    00000 00000 0   0 0   0 0  00
(psiman)
- INSTALLER EDITION -

v2.1.1

A blob that installs psiman (the cli-wrapper
for psilib), and psilib.

Copyright (c) 2019 Ong Yong Xin
Open-sourced under the MIT License.

Source:
https://github.com/sn3ksoftware/psiman
"""

# Import needed modules.
import json
import os
import sys
import requests
import zipfile
import zlib
import platform
import shutil
import inspect

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
            inslist = ["~/Library/scripts", "~/Library/psicfg", "Libterm"]
            return inslist
        else:
            # Running on Pythonista, check if StaSh is installed.
            try:
                import stash
            except ImportError:
                print("\nE: StaSh is not installed. Please install StaSh first with [import requests as r; exec(r.get('https://bit.ly/get-stash').text)].")
                exit()
            else:
                print("\nInstaller is running on Pythonista, StaSh is installed.")
                inslist = ["~/Documents/bin", "~/Documents/.psicfg", "Pythonista"]
                return inslist
    else:
        # Not running on iOS: Platform not supported.
        print("\nE: Your platform is not supported.")

# Declare needed vars.
paths = chkplat()
script_p = os.path.expanduser(paths[0])
psicfg_p = os.path.expanduser(paths[1])
tmp = psicfg_p + "/tmp/"
site_packages = next(p for p in sys.path if 'site-packages' in p)
plat = paths[2]

# Make needed folders.
def mkfolder():
    if os.path.isdir(psicfg_p):
        print(
        """
        E: psicfg folder already exists at the install location.
        Use psiman's inbuilt update command to update to a newer version.
        """
        )
    else:
        try:
            os.mkdir(psicfg_p)
            os.mkdir(psicfg_p + "/repo")
            os.mkdir(psicfg_p + "/json")
            os.mkdir(psicfg_p + "/tmp")
        except OSError as e:
            print("\nE: OSError encountered! Error: " + e.strerror)
        else:
            print("\nOK: Config directories created at " + psicfg_p + ".")

# Create repolist.json in .psicfg/repo.
def createjson():
    print("\nCreating repolist...")
    dict = {
        "mainrepo": "https://raw.githubusercontent.com/sn3ksoftware/psidex/master/index.json",
        "repolist": ["https://raw.githubusercontent.com/sn3ksoftware/psidex/master/index.json"]
    }
    with open(psicfg_p + "/repo/repolist.json", "w") as f:
        json.dump(dict, f)
    print("\nDone.")

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

# Download psiman from repo and unzip to script folder.
def getpsi():
    print("\nStarting install of psiman...")
    mkfolder()
    createjson()
    print("\nGetting psiman from sn3ksoftware/psiman...")
    dl("https://raw.githubusercontent.com/sn3ksoftware/psiman/master/psiman.py", path=tmp)
    dl("https://raw.githubusercontent.com/sn3ksoftware/psilib/master/psilib.zip", path=tmp)
    # Extract psilib to site-packages, and
    # move psiman.py to script path.
    # If user specifes [-m] option, install
    # psilib module only.
    if chkarg1():
        if sys.argv[1] == "-m":
            extractfile(tmp + "psilib.zip", site_packages)
            print("\nInstalled psilib only.")
        else:
            try:
                shutil.move(tmp + "psiman.py", script_p)
            except shutil.Error:
                print("\nW: psiman already exists.\nReplacing...")
                os.remove(script_p + "/psiman.py")
                shutil.move(tmp + "psiman.py", script_p)
            # Clean up tmp folder
            for file in os.listdir(tmp):
                tmpfile = os.path.join(tmp, file)
                os.remove(tmpfile)
            print("\nInstalled both psiman and psilib.")

if __name__ == '__main__':
    getpsi()