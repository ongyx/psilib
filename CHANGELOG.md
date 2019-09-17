# Changelog

### psilib v3.3.0-alpha:
- Indexes are now downloaded for all repos at once. This means that there is no need to switch repos to get certain packages. (Also, the upgrade function now works.)
- This incidentally also removes the need for psilib.repo.set().
- psilib.repo.fetch() has been moved to psilib.repo.update().
- psilib.repo.update() now returns True if all indexes were downloaded sucessfully.
- Package installation was broken due to different possible configurations for the Script Definition file. It now uses ywangd’s original system.

### psilib v3.2.0-alpha:
- Alpha-stage support for ywangd's older implementation of the Pythonista Script
Index. Because of the inconsistency of package formats, this is VERY unstable
and NOT gurenteed to work or install command-line scripts. More support will be added
to a new bugfix later on (problably v3.2.1-alpha.)
- Added support for packages hosted within a Github Gist. Does not work on muiti-file
gists.
- Packages can now be one of these formats: a singular .py or .pyui file, or
a zipfile (that can contain dev-specific dependencies).
The `type` key in the script.json file must be set to either 'module' or 'script'.
(Scripts will be extracted/moved to `psilib.config.script_store`, and modules
extracted to `psilib.config.site_packages`.
- Using `psiman setrepo` will now automatically download the index from the new repo.

### psilib v3.1.0-alpha:
- Lots of bugfixes for both psilib and
the psiman cli-wrapper.
- psilib now supports semantic versioning as package versions.
- Package versions are now compared to a local file (versions.json) so that packages will NOT be redownloaded if the package in the repo is at the same version as the local counterpart.
- Packages will be installed to site-packages if it is a module.
- New function, psilib.package.upgrade(), which downloads and installs all packages with a newer version available in the repository.
- New function, psilib.package.search(), that finds/lists packages based on name, type(module/script), and branch(stable/rolling).
- psiman.repo.set() and psiman.repo.rem() are now non-interactive.
Use psiman.repo.list() to list repos in repolist and then pass the 'N'th
repository number to set() and rem().

### psilib v3.0.0-alpha:
THE MODULAR UPDATE
The singular psiman script has now been split
into two: A backend library (psilib) that
handles low-level functions and a frontend
script (psiman) that interfaces with psilib.
The split was done as:
- The code is now easier to debug as it is
not a continueous wall of text.
- It allows package installs, etc. to be scripted.
- psilib can have seperate dev cycles from
psiman, and vice versa.
- New functions can be updated easily.
