"""
Temp_template

File name : Template.py
Authors   : Eric Liu
Time      : 2022-09-14, 03:36
Version   : 0.1.0
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

RAW_STR = "{}_{}\n\n" \
    "Time : {}\n" \
    "Author : {}\n" \
    "Description : {}"


def getpwd():
    """_summary_

    Returns:
        _type_: _description_
    """
    # root = os.getcwd()
    root = os.path.abspath(__file__)
    basename = os.path.basename(__file__)
    if root.split('/')[-2] == 'utils':
        return root.replace('/utils/' + basename, '/')


def print_version():
    """_summary_
    """
    with open(getpwd() + '/VERSION', 'r', encoding='utf-8') as file:
        print(file.readline())
        file.close()


def touch_info():
    """_summary_
    """

    def touch_file(text):
        file_name = getpwd() + text + '/INFO'
        project_name = getpwd().split('/')[-1]
        print(file_name)
        with open(file_name, 'w', encoding='utf-8') as file:
            input_text = RAW_STR.format(project_name, text, \
                time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                                        os.getlogin(), DESCRIPTION[text])
            file.write(input_text)
            file.close()

    output = [dI for dI in os.listdir(getpwd()) if os.path.isdir(os.path.join(getpwd(), dI))]
    dirs = [dir for dir in output if dir[0] != '.']
    for dir_name in dirs:
        touch_file(dir_name)


def refresh():
    """_summary_
    """
    os.rmdir(getpwd() + '/build')
    os.system("catkin_make")
    print("Refreshed project")


def print_help():
    """_summary_
    """
    print("\nPlease use this commond \n    python template.py -{r/i/v/h} \n")
    print_expression = \
        "     -r, --refresh       : refresh\n" \
        "     -h, --help          : help\n" \
        "     -i, --install_info  : create information\n" \
        "     -v, --version       : print version\n"
    print(print_expression)


if __name__ == '__main__':
    params = sys.argv
    if len(params) != 2:
        print_help()
    else:
        param = params[1]
        if param == '-r' or param == '--refresh':
            refresh()
        elif param == '-h' or param == '--help':
            print_help()
        elif param == '-i' or param == '--install_info':
            print("install info")
            touch_info()
        elif param == '-v' or param == '--version':
            print_version()
