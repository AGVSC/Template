#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
Template_template

File name : Template.py
Authors   : Eric Liu
Time      : 2022-09-14, 03:36
Version   : 0.1.4
"""

import shutil
import sys
import os
import time

DESCRIPTION = {
    "build": "Files built in the runtime",
    "include": "Header files",
    "lib": "Library files",
    "src": "Source files",
    "assets": "Resource files",
    "app": "Application files",
    "third_party": "Third party repos",
    "utils": "Utilitys script files",
    "cfg": "ROS configure files",
    "launch": "ROS launch files",
    "msg": "ROS message files",
    "rviz": "ROS rviz files",
    "scripts": "ROS scripts files",
    "srv": "ROS service files"
}

# ${PROJECT_NAME}_${DIR_NAME}
RAW_STR = \
    "{}_{}\n\n"  \
    "Time : {}\n" \
    "Author : {}\n" \
    "Description : {}\n" \
    "Version : {}"

EXPRESSION = "\n" \
        "Please use this commond \n" \
        "    python template.py -{f/h/i/r/v} \n" \
        "     -f, --refresh       : refresh\n" \
        "     -h, --help          : help\n" \
        "     -i, --install_info  : create all INFO\n" \
        "     -r, --remove        : remove all INFO\n" \
        "     -v, --version       : print version\n"

FILE_NAME = '/.INFO'


def get_root():
    """
    getroot :
        Get root directory.

    Returns
    ---------
    root_str : Str
            Absolute path to the root file where the repository is located.
    """
    root = os.path.abspath(__file__)
    basename = os.path.basename(__file__)
    if root.split('/')[-2] == 'utils':
        root_path = root.replace('/utils/' + basename, '/')
        # print("root_path", root_path)
        return root_path


def find_all_dirs():
    """
    find_all_dirs :
        Find all secondary directories' name.

    Returns
    ---------
    dirs : list(Str)
        A list with all secondary directories' name
    """
    root_dir = get_root()
    dirs = [dir for dir in os.listdir(root_dir) \
            if os.path.isdir(os.path.join(root_dir, dir)) \
                and dir[0] != '.']
    return dirs


def get_version():
    """
    get_version :
         Get version info in '../VERSION' file.

    Returns
    ---------
    file_ver : Str
        File version
    """
    with open(get_root() + '/VERSION', 'r', encoding='utf-8') as file:
        file_ver = file.readline()
        file.close()
        return file_ver


def install_info():
    """
    install_info :
        Create some INFO files and put them in every secondary root directorys.
        Every INFO files will be written in a 'RAW_STR' string var.
        Also you can modify it when you have other needs indeed.

    Returns
    ---------
    num : Int
        Number of folders in the root directory.
    """
    root_dir = get_root()

    def install_file(text):
        file_name = root_dir + text + FILE_NAME
        project_name = root_dir.split('/')[-2]
        if text in DESCRIPTION:
            with open(file_name, 'w', encoding='utf-8') as file:
                input_text = RAW_STR.format(project_name, text, \
                    time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        os.getlogin(), DESCRIPTION[text], get_version())
                file.write(input_text)
                file.close()
        else:
            print(f"dir_name {text} is not essentional")

    dirs = find_all_dirs()
    for dir_name in dirs:
        install_file(dir_name)
    return len(dirs)


def refresh():
    """
    refresh :
        Remove 'build' directory and re=build it.
        Always using 'catkin_make' command.
    """
    os.rmdir(get_root() + '/build')
    os.system("catkin_make")


def print_help():
    """ print_help : printf help info stored in the 'EXPRESSION' string var. """
    print(EXPRESSION)


def remove_info():
    """
    remove_info :
        Remove every INFO file in every secondary root directories if they existed.
        Remove 'build' directory if it exists.

    Returns
    ---------
    count : Int
        Number of folders in the root directory, which has INFO file.
    """
    dirs = find_all_dirs()
    base_name = get_root()
    build_dir = base_name + 'build'
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    count = 0
    for dir_name in dirs:
        file_name = base_name + dir_name + FILE_NAME
        if os.path.exists(file_name):
            os.remove(file_name)
            count += 1

    return count


def test_fun():
    """
    test_fun _summary_ : Test function.
    """
    print("Test ended")


if __name__ == '__main__':
    PARAMS = sys.argv
    if len(PARAMS) != 2:
        print_help()
    else:
        PARAM = PARAMS[1]
        if PARAM in ('-f', '--refresh', 'f', 'refresh'):
            refresh()
            print("Refreshed project")
        elif PARAM in ('-h', '--help', 'h', 'help'):
            print_help()
        elif PARAM in ('-i', '--install_info', 'i', 'install'):
            print(f"Installed info in {install_info()} folders at {get_root()}")
        elif PARAM in ('-v', '--version', 'v', 'version'):
            print(get_version())
        elif PARAM in ('-r', '--remove', 'r', 'remove'):
            print(f"Remove info in {remove_info()} folders at {get_root()}")
        elif PARAM in ('-t', '--test', 't', 'test'):
            test_fun()
        else:
            print(f"Unused param : {PARAMS[1]} \nUser input : {PARAMS[0]} {PARAMS[1]}")
            print_help()
