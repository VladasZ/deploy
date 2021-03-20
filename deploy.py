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


def linux_setup():
    print("Linux setup")
    run("sudo apt-get update")
    run("sudo apt-get install python3-pip")
    run("sudo apt-get install libgl1-mesa-dev")
    run("sudo apt-get install libgl1-mesa-dri")
    run("sudo pip3 install setuptools -U")
    run("sudo pip install conan")
    run("sudo pip install wheel")
    run("export PYTHONPATH=\"${PYTHONPATH}:" + build_tools_path + "\"")
    run("gcc --version")


def windows_setup():
    print("Windows setup")
    run("pip install conan")


def mac_setup():
    print("Mac setup")
    run("pip3 install conan")
    run("clang --version")


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

#setup_alacritty()
