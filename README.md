<p align="center">
  <b> psilib </b> &bull;
  <a href="https://github.com/sn3ksoftware/psicli">psicli</a> &bull;
    <a href="https://github.com/sn3ksoftware/psidex">psidex</a>
</p>

# psilib: The json-based backend for the psiman package manager
(formerly [spkg for Libterm](https://github.com/sn3ksoftware/sandpkg/tree/testing))

<img src="https://raw.githubusercontent.com/sn3ksoftware/psilib/master/psilib_logo.png" alt="psiman_logo:Ψ" width="200"/>

Welcome to the repo for psilib, a json-based backend for the [psiman](https://github.com/sn3ksoftware/psiman) package manager.

It uses the [psidex](https://github.com/sn3ksoftware/psidex) system to distribute packages.

Platforms supported:

| Platform  | Version of psilib |
| --- | --- |
| [Libterm](https://github.com/ColdGrub1384/LibTerm) | ![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/sn3ksoftware/psilib?include_prereleases&sort=semver) |
| [Pythonista](http://omz-software.com/pythonista/) | ![GitHub release (latest SemVer including pre-releases)](https://img.shields.io/github/v/release/sn3ksoftware/psilib?include_prereleases&sort=semver) |
| Linux (Generic) | -WIP- |
| Windows | -WIP- |

For more info, take a look at the [documentation](https://github.com/sn3ksoftware/psilib/wiki).

# TODO
The list below is as follows:

**(M)** denotes a major change to psilib/psiman code.

**(m)** denotes a minor change to psilib/psiman code.

**(p)** denotes a patch for a bug within psilib/psiman code.

- [x] (M) Add semantic versioning to psilib.package.install()
- [ ] (M) Add code to handle dependencies
- [x] (M) Implement the whole Pythonista Script Index specification, i.e support multiple 
packages using the same json file
- [ ] (M) Get psilib to a stable API release (0.1.0)
- [ ] (M) Add global cache to store indexes of muitiple repos (i.e, no need to switch repositories.)
- [x] (m) Make setrepo() and delrepo() non-interactive 
- [x] (m) Update meta-version in all packages to reflect API changes
- [x] (p) Make the cli-wrapper for psilib(psiman) less buggy
- [x] (p) Format output of the cli-wrapper properly

# P.S
The code from [spkg for Libterm](https://github.com/sn3ksoftware/sandpkg/tree/testing) was _heavily_ modified to use the json-based `psidex` system.
Its original source code, including the psiman package manager, is under the MIT License.
