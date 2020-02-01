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

def run(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()

def clone(rep, destination = ""):
	if not os.path.exists(destination):
		run("git clone --recursive https://github.com/vladasz/" + rep + " " + destination)

def linux_setup():
    print("Linux setup")

    run("sudo add-apt-repository ppa:jonathonf/python-3.6")
    run("sudo apt-get update")
    run("sudo apt-get install python3.6")
    run("sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1")
    run("sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2")
    run("sudo update-alternatives --config python3")
    run("python3 -V")
    run("sudo apt-get install python3-pip")
    run("sudo pip3 install setuptools -U")
    run("sudo pip3 install conan")
    run("sudo pip3 install wheel")
    run("export PYTHONPATH=\"${PYTHONPATH}:" + build_tools_path + "\"")

def windows_setup():
    print("Windows setup")
    run("pip install conan")

def mac_setup():
    print("Mac setup")
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
