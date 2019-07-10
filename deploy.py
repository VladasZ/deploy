#!/usr/bin/env python3

import os
import platform

is_windows = platform.system() == "Windows"
is_mac     = platform.system() == "Darwin"
is_linux   = platform.system() == "Linux"

python_cmd = "py "  if is_windows else "python3 "
pip_cmd    = "pip " if is_windows else "pip3 "

home = os.path.expanduser("~/")
deps_path = home + ".deps/"
build_tools_path = deps_path + "build_tools/"
shell_path = home + ".shell/"

def run(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()

def clone(rep, destination = ""):
    run("git clone --recursive https://github.com/vladasz/" + rep + " " + destination)

clone(".shell",      shell_path)
clone("build_tools", build_tools_path)

os.environ["PATH"]       += shell_path
#os.environ["PYTHONPATH"]  = build_tools_path

run("export PYTHONPATH=${PYTHONPATH}:" + build_tools_path)
run("echo ${PYTHONPATH}")
run("echo ${PATH}")

print(home)
