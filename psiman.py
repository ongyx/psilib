#!/usr/bin/env python3

"""
0000  00000 00000 0   0   0   00  0
00  0 00      0   00 00  0 0  00  0
00000 00000   0   0 0 0 00000 0 0 0
00       00   0   0   0 0   0 0  00
00    00000 00000 0   0 0   0 0  00
(psiman)
The cli-wrapper for psilib, allowing use
from the command-line.

Copyright (c) 2019 Ong Yong Xin
Open-sourced under the MIT License.
To print out the license, execute the below:
import psilib as psi; psi.misc.license()

Source:
https://github.com/sn3ksoftware/psiman
"""

# Import functions from stdlib
import sys
from inspect import getargspec

# Import functions from psilib
from psilib.repo import add, set, rem, fetch
from psilib.package import install, remove, list, desc
from psilib.misc import credits, license
from psilib.utils import ansi

# If there are no arguements, provide user help
def getParameters(args):
    if len(args) == 1:
        print(
        "\nusage: psiman (action) [options] <input>\n"
        "Type [psiman -h] for help.\n"
        )
        return None
    else:
        arg1_raw = (sys.argv[1])
        return(arg1_raw)

# Get first arguement from params
arg1 = getParameters(sys.argv)
argall = sys.argv

# Declare wrapper-specific variables.
invalid_cmd = ansi(31) + '\nE: Invalid/unknown command. Try again.\n\nusage: psiman [options]\nType [spkg -h] for help.\n' + ansi(0)

# Dictionary used to map functions.
func_dict = {
    "-h": "help",
    "-c": "credits",
    "-ar": "add",
    "-sr": "set",
    "-dr": "rem",
    "-i": "install",
    "-r": "remove",
    "-l": "list",
    "-d": "desc",
    "-f": "fetch",
}

# Help function. This is specific to the wrapper itself.
def help():
    print(
    """
Printing help...
\n-PACKAGE MANAGEMENT-\n
\t[-i], {package}: Install new packages.
\t[-r], {package}: Remove specified package.
\t[-l], <repo/lcl>: List packages in repo/installed packages.
\t[-d], {package}: Print description of package specified(if any).
\n-REPOSITORY MANAGEMENT-\n
\t[-ar], {repo}: Adds new repository.
\t[-sr]: Sets main repository to use.
\t[-dr]: Removes repository from local list.
\t[-f]: Fetch latest index file from main repository.
\n-MISCELLANEOUS-\n
\t[-init], <repo/pkg>: Restores repo to defaults/deletes\n\tall spkg-installed packages(wip).
\t[-h]: Prints help screen.
\t[-c]: Print version and credits.
    """
    )


# Define main function.
def main():
    # Try to get function name. If it fails, print a error message.
    try:
        cmd_name = func_dict[arg1]
    except KeyError:
        if len(sys.argv) == 1:
            pass
        else:
            print(invalid_cmd)
    else:
        # Check if function requires args.
        # By default, sys.argv[2] will be
        # passed to the function.
        func = eval(cmd_name)
        try:
            if func() == None:
                pass
            else:
                print(func())
        except TypeError:
            try:
                print(func(sys.argv[2]))
            except IndexError:
                print(ansi(31))
                print(
                f"E: action {cmd_name} requires input, i.e\n"
                f"psiman {arg1} <input>\n"
                "Type (psiman -h) for more info."
                )
                print(ansi(0))

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
