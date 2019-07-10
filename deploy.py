#!/usr/bin/env python3

import os
import platform

is_windows = platform.system() == "Windows"
is_mac     = platform.system() == "Darwin"
is_linux   = platform.system() == "Linux"

home             = os.path.expanduser("~/")
build_tools_path = home + ".deps/build_tools/"
shell_path       = home + ".shell/"

def run(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()

def clone(rep, destination = ""):
    run("git clone --recursive https://github.com/vladasz/" + rep + " " + destination)

def linux_setup():
    print("Linux setup")
    run("sudo apt install python3-pip")
    run("sudo apt install python3-setuptools")
    run("sudo pip3 install conan")

def windows_setup():
    print("Windows setup")

def mac_setup():
    print("Mac setup")
    run("pip3 install conan")
    
clone(".shell",      shell_path)
clone("build_tools", build_tools_path)

if is_windows:
    windows_setup()
elif is_mac:
    mac_setup()
elif is_linux:
    linux_setup()
else:
    print("Unknown os")

    
