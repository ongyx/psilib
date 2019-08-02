# Installer for psiman(Libterm)
# Code by Ong Yong Xin, ©️2019
# Licenced under MIT License.
# v2.00

# Import needed modules.
import json, os, requests, zipfile, zlib, platform

# Check install platform
def chkplat():
    if platform.machine().startswith("iP")
    # iOS
        try:
            import ui
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
                inslist = ["~/Documents/bin", "~/Library/psicfg", "Pythonista"]
                return inslist
    else:
        # Not running on iOS, other platforms not supported yet.
        print("\nE: This installer does not support your platform yet.")

# Declare needed vars.
paths = chkplat()
script_p = paths[0]
psicfg_p = paths[1]
plat = paths[2]

# Make needed folders.
def mkfolder():
    if os.path.isdir(psicfg_p):
        print("\nE: psicfg folder already exists at the install location. Use psiman's inbuilt update command to update to a newer version.")
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
        "mainrepo": "https://raw.githubusercontent.com/sn3ksoftware/psidex/index.json",
        "repolist": ["https://raw.githubusercontent.com/sn3ksoftware/psidex/index.json"]
    }
    with open(psicfg_p + "/repo/repolist.json", "w") as f:
        json.dump(dict, f)
    print("\nDone.")

# Define extractfile function
# Copied from zip2 command
def extractfile():
    print("\nExtracting...")
    with zipfile.ZipFile(psicfg_p + "/tmp/psiman.zip", 'r') as zip:
        try:
            zip.extractall(path=script_p)
        except zipfile.BadZipfile:
            print("\nE: Zip file is bad (corrupted?)\nAbort.")
        else:
            print("\nSucessfully extracted psiman to scripts.")

# Define download function.
def dl(url):
    psifile = requests.get(url).content
    with open(psicfg_p + "/tmp/psiman.zip", "wb") as f:
         f.write(psifile)

# Download psiman from repo and unzip to script folder.
def getpsi():
    print("\nStarting install of psiman...")
    mkfolder()
    createjson()
    print("\nGetting psiman from sn3ksoftware/psiman...")
    if plat == "Pythonista":
        dl("https://raw.githubusercontent.com/sn3ksoftware/psiman/master/psiman_pythonista.zip")
    else:
        print("\nInstalling to ~/Library/scripts...")
        dl("https://raw.githubusercontent.com/sn3ksoftware/psiman/master/psiman_libterm.zip")
    extractfile()
    print("\nDone.")

if __name__ == '__main__':
    getpsi()