# Create a repo

1. Create the `${WORKSPACE}` folder as your WORKSPACE file directory. Create the `src` folder and go to the `${WORKSPACE}` folder and run the 'catkin_init_workspace' command.
2. Create a remote code repository and clone it in the `${WORKSPACE}/src` path
3. Modify the base file, such as `.gitignore` `readme.md`, etc., and then commit
4. Create a ROS package. If the package is a ROS package:
   1. `catkin_create_pkg <agv-${REPONAME}> <roscpp ...>`.
   2. Modify the information file, such as `package.xml` `cmakelists.txt` and so on.
   3. Code and commit with formator.
5. You can run `python3./utils/template.py [OPTION]` under `${REPONAME}` for partial operations.
6. Periodically use Changelog-generater to generate and update `changelog.md`.

## style check

- cpp : cpplint(Google)
- python : yapf(pep8)
- markdown : markdownlint
- git commit : commitlint

## Submit the specification

Use Commitizen to make a commit
(In VSC, you can use `Ctrl+Shift+P` and input `convention commits`, then type as prompted)
