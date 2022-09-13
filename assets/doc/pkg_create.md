# Create a meta package

1. Create a repo in your git website.
2. Clone your repo and modify some files, such as `.gitignore` `README.md`, then run `git commit`.
3. Create ROS pack, if this pack is a ros meta pack.
   1. `catkin_create_pkg <agv-${name}> <roscpp ...>`
   2. Modify some files, such as `package.xml` `CMakeLists.txt` and so on.
   3. Code.
   4. Use this command `python utils/template.py -i`.
