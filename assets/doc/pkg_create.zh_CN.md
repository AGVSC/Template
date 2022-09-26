# 仓库创建过程

## 新建仓库流程

1. 建立文件夹`${WORKSPACE}`当作你的工作区文件目录，建立`src`文件夹。进入`${WORKSPACE}`文件夹后执行命令`catkin_init_workspace`
2. 创建一个远程代码仓库，并克隆到`${WORKSPACE}/src`路径下
3. 修改基础文件，如`.gitignore` `README.md`等，然后进行提交
4. 创建ROS包， 如果该包是ROS包的情况下：
   1. `catkin_create_pkg <agv-${REPONAME}> <roscpp ...>`
   2. 修改信息文件，如`package.xml` `CMakeLists.txt`等等
   3. 编码并按格式提交
5. 在`${REPONAME}`路径下可以执行`python3 ./utils/template.py [OPTION]`进行部分操作
6. 定时使用ChangeLog-Generater进行`changelog.md`的生成与更新

## 编码规范检查

- cpp : cpplint(Google)
- python : yapf(pep8)
- markdown : markdownlint
- git commit : commitlint

## 提交规范

使用commitizen进行commit提交
（在VSC中，你可以按下`Ctrl+Shift+P`，输入`convention commits`，之后根据提示即可
