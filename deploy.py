#!/usr/bin/env python3

import os
import shutil
import platform

is_windows = platform.system() == "Windows"
is_mac     = platform.system() == "Darwin"
is_linux   = platform.system() == "Linux"

unix = is_mac or is_linux


def _get_home():
    if "HOME" in os.environ:
        return os.environ["HOME"]
    return os.path.expanduser("~")
    

home = _get_home()

build_tools_path = home + "/.deps/build_tools/"
shell_path       = home + "/.shell/"
deploy_path      = home + "/deploy"


def copy(src, dst):
    print("Copying:\n" + src + " to:\n" + dst)
    if os.path.isfile(src):
        shutil.copyfile(src, dst)
    else:
        shutil.copytree(src, dst)


def run(string):
    print(string)
    if os.system(string):
        print("Shell script has failed")
        exit()


def clone(rep, destination = ""):
    if not os.path.exists(destination):
        run("git clone --recursive https://github.com/vladasz/" + rep + " " + destination)


def alacrittyTargetPath():
    if unix:
        return home + "/.alacritty.yml"
    print(os.environ["APPDATA"])
    return os.environ["APPDATA"] + "/alacritty/alacritty.yml"


def alacrittyLocalPath():
    suffix = ""
    if is_mac:
        suffix = "mac"
    elif is_linux:
        suffix = "lin"
    elif is_windows:
        suffix = "win"
    else:
        raise Exception("Unknown os")
    return deploy_path + "/alacritty/alacritty_" + suffix + ".yml"


def setup_alacritty():
    copy(alacrittyLocalPath(), alacrittyTargetPath())


clone(".shell",      shell_path)
clone("build_tools", build_tools_path)

setup_alacritty()
