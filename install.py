# Installer for psiman(Libterm)
# Code by Ong Yong Xin, ©️2019
# Licenced under MIT License.

# Import needed modules.
import json, os, requests, zipfile, zlib

# Declare needed vars.
# By default, psiman installs its config files here.
# If changed, please edit psiman's psicfg_path to match the one below.
script_p = os.path.expanduser("~/Library/scripts")
psicfg_p = os.path.expanduser("~/Library/psicfg")

# Make needed folders.
def mkfolder():
    if os.path.isdir(psicfg_p):
        print("\nE: psicfg folder already exists at the install location. Use psiman's inbuilt update command ti update to a newer version.")
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

# Download psiman from repo and unzip to ~/Library/scripts folder.
def getpsi():
    print("\nStarting install of psiman...")
    mkfolder()
    createjson()
    print("\nGetting psiman from sn3ksoftware/psiman...")
    url = "https://raw.githubusercontent.com/sn3ksoftware/psiman/master/psiman.zip"
    psifile = requests.get(url).content
    with open(psicfg_p + "/tmp/psiman.zip", "wb") as f:
        f.write(psifile)
    print("\nInstalling to ~/Library/scripts...")
    extractfile()
    print("\nDone.")

if __name__ == '__main__':
    getpsi()