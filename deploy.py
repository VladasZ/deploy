#!/usr/bin/env python3

import os
import shutil
import platform

is_windows = platform.system() == "Windows"
is_mac     = platform.system() == "Darwin"
is_linux   = platform.system() == "Linux"

home             = os.path.expanduser("~/")
build_tools_path = home + ".deps/build_tools/"
shell_path       = home + ".shell/"

print("HELLOPOPPPP")

def run(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()

def clone(rep, destination = ""):
	if not os.path.exists(destination):
		run("git clone --recursive https://github.com/vladasz/" + rep + " " + destination)

def copy_conan_profile():
	shutil.copyfile("./deploy/conan/ios", home + ".conan/profiles/ios")

def linux_setup():
    print("Linux setup")
    copy_conan_profile()
    run("sudo apt install python3-pip")
    run("sudo apt install python3-setuptools")
    run("sudo pip3 install conan")

def windows_setup():
    print("Windows setup")
    copy_conan_profile()
    run("git submodule update --init --recursive")
    run("pip install conan")

def mac_setup():
    print("Mac setup")
    copy_conan_profile()
    run("pip3 install conan")

if is_windows:
    windows_setup()
elif is_mac:
    mac_setup()
elif is_linux:
    linux_setup()
else:
    print("Unknown os")
    
clone(".shell",      shell_path)
clone("build_tools", build_tools_path)
