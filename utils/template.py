"""
Temp_template

File name : Template.py
Authors   : Eric Liu
Time      : 2022-09-14, 03:36
Version   : 0.1.2
"""

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
    "Description : {}"

EXPRESSION = "\n" \
        "Please use this commond \n" \
        "    python template.py -{f/h/i/r/v} \n" \
        "     -f, --refresh       : refresh\n" \
        "     -h, --help          : help\n" \
        "     -i, --install_info  : create all INFO\n" \
        "     -r, --remove        : remove all INFO\n" \
        "     -v, --version       : print version\n"


def getroot():
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
        # print(root_path)
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
    dirs = [dir for dir in os.listdir(getroot()) \
            if os.path.isdir(os.path.join(getroot(), dir)) \
                and dir[0] != '.']
    return dirs


def print_version():
    """ print_version : Print version info in '../VERSION' file. """
    with open(getroot() + '/VERSION', 'r', encoding='utf-8') as file:
        print(file.readline())
        file.close()


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

    def install_file(text):
        file_name = getroot() + text + '/INFO'
        project_name = getroot().split('/')[-2]
        print(file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            input_text = RAW_STR.format(project_name, text, \
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        os.getlogin(), DESCRIPTION[text])
            file.write(input_text)
            file.close()

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
    os.rmdir(getroot() + '/build')
    os.system("catkin_make")


def print_help():
    """ print_help : printf help info stored in the 'EXPRESSION' string var. """
    print(EXPRESSION)


def remove_info():
    """
    remove_info :
        Remove ervery INFO file in every secondary root directorys if they existed.

    Returns
    ---------
    count : Int
        Number of folders in the root directory, which has INFO file.
    """
    dirs = find_all_dirs()
    base_name = getroot()
    count = 0
    for dir_name in dirs:
        file_name = base_name + dir_name + '/INFO'
        # print(file_name)
        if os.path.exists(file_name):
            os.remove(file_name)
            count += 1
    return count


if __name__ == '__main__':
    params = sys.argv
    if len(params) != 2:
        print_help()
    else:
        param = params[1]
        if param in ('-f', '--refresh', 'f', 'refresh'):
            refresh()
            print("Refreshed project")
        elif param in ('-h', '--help', 'h', 'help'):
            print_help()
        elif param in ('-i', '--install_info', 'i', 'install'):
            print(f"Installed info in {install_info()} folders at {getroot()}")
        elif param in ('-v', '--version', 'v', 'version'):
            print_version()
        elif param in ('-r', '--remove', 'r', 'remove'):
            print(f"Remove info in {remove_info()} folders at {getroot()}")
        else:
            print(f"\nUser input : {params[0]} {params[1]} \n")
            print_help()