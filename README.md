<p align="center">
  <b> psiman </b> &bull;
  <a href="https://github.com/sn3ksoftware/psidex">psidex</a> &bull;
    <a href="https://github.com/sn3ksoftware/sandpkg">sandpkg</a>
</p>

# psiman: The PSIdex package MANager
(formerly [spkg for Libterm](https://github.com/sn3ksoftware/sandpkg/tree/testing))

![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/sn3ksoftware/psiman?include_prereleases&sort=semver)

<img src="https://raw.githubusercontent.com/sn3ksoftware/psiman/master/psiman_logo.png" alt="psiman_logo:Ψ" width="200"/>

Welcome to the repo for psiman, a json-based package manager that uses the [psidex](https://github.com/sn3ksoftware/psidex) system.

Platforms supported:

| Platform  | Version  |
| --- | --- |
| [Libterm](https://github.com/ColdGrub1384/LibTerm) | v3.0.0a |
| [Pythonista](http://omz-software.com/pythonista/) | v3.0.0a |
| Linux (Generic) | -WIP- |
| Windows | -WIP- |

(More platforms will be added as needed.)
# Dependencies
psiman, of course, requires Python 3.5+.
It only requires stlib that comes with Python 3.5+ and the requests library (preinstalled on Pythonista and Libterm), so it should work out of the box.
For Pythonista, [StaSh](https://github.com/ywangd/stash) is required to run psiman.
Install with `import requests as r; exec(r.get('https://bit.ly/get-stash').text)`.
# Installation
## Libterm:
Download the installer and run it.
```
curl -O https://raw.githubusercontent.com/sn3ksoftware/psiman/master/install.py
python install.py
```
## Pythonista:
Open the Python interpreter (under `Console`) and run the command below. (Method copied from StaSh)
```
import requests as r; exec(r.get('https://raw.githubusercontent.com/sn3ksoftware/psiman/master/install.py').text)
```
Configuration files are, by default, stored at `~/Documents/.psicfg`.
# Features:
* A decentralised repository system, where the package authors are also the repo maintainers.
* Schemes can be added to psiman, depending on the repo host. You might even be able to use non-conventional methods (like Google Drive) to host repos in this system!
* Their repos/packages appear as minimal entries to the main index.json file. From there, psiman will seek out the package through the listings.
* Fully written in Python from the bottom-up, only using modules from stdlib. 
* Because it does not use any platform-specific modules, it is easy to port over to other *Nix-in-a-Box apps (i.e, [Libterm](https://github.com/ColdGrub1384/LibTerm)), or pure Python apps (i.e, [Pythonista](http://omz-software.com/pythonista/)).
* Easy package management, where entries for dependencies/description/author are stored in one file.
For an example of the main index.json file in the [psidex](https://github.com/sn3ksoftware/psidex) repo, here it is (copied from ywangd’s spec):
```json
{
    "meta_version": "1.0",
    "name": "Pythonista Script Index",
    "website": "https://github.com/...",

    "scripts": {
        "A_script": {
            "meta_url": "https://github.com/person/repo/info.json",
        },

        "B_script": {
            "meta_url": "https://github.com/someone/somerepo/info.json#B_script",
        }
    }
    
}
```
`meta_version` contains the version number (set according to semantic versioning);
and `meta_url` containing the location of the script sub-index file (for every script entry).
This way, part of the repo management is pushed to the package authors, making it easier to update
their packages regularly.

Then, there is the Script sub-index file (package/script.json):
```json
{
    "meta_version": "1.0",  
    "name": "An awesome script",
    "author": "First Last",
    "email": "email@test.com",
    "website": "https://...",
    "description": "he is too awesome",

    "releases": [ 
        {
            "version": "1.0", 
            "url": "https://.../a_script.py"
        },

        {
            "version": "2.0", 
            "url": "https://.../a_script.zip”
        },
    ]
}
```
As you can see, there is _vastly_ more infomation stored here.
This includes more info on a specific package (author, desc., versions available, etc.)
Also note that this script sub-index also has a semantic version number, which allows for
parsing to be done diffrently based on it’s version number.

(All this will be moved to a wiki soon.)
# TODO
The list below is as follows:

**(M)** denotes a major change to psilib/psiman code.

**(m)** denotes a minor change to psilib/psiman code.

**(p)** denotes a patch for a bug within psilib/psiman code.

- [ ] (M) Add semantic versioning to psilib.package.install()
- [ ] (M) Add code to handle dependencies
- [ ] (M) Implement the whole Pythonista Script Index specification, i.e support
packages using the same json file
- [ ] (M) Get psilib to a stable API release (0.1.0)
- [ ] (m) Make setrepo() and delrepo() non-interactive 
- [ ] (m) Update meta-version in all packages to reflect API changes
- [ ] (p) Make the cli-wrapper for psilib(psiman) less buggy
- [x] (p) Format output of the cli-wrapper properly

# P.S
The code from [spkg for Libterm](https://github.com/sn3ksoftware/sandpkg/tree/testing) was _heavily_ modified to use the json-based `psidex` system.
Its original source code, including the psiman package manager, is under the MIT License.
