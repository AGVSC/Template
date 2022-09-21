# 模板库

---

## 描述

该库是AGVSC通用模板库，它规定了一系列库的编码规范和文件结构，在构建其他库时，起到导向和约束作用，从而进行快速开发。

- 遵循`assets/doc/pkg_create.md`进行仓库建立与开发
- 遵循`assets/doc/style_guide.md`进行代码编写与样式检查

## IDE

使用Ubunt20.04下的Visual Studio Code进行开发，请根据相关脚本文件配置所需开发环境

## 依赖

- ROS noetic

  - [参考链接](http://wiki.ros.org/noetic/Installation/Ubuntu)

- cpplint

  ```shell
  sudo pip3 install cpplint
  ```

- yapf

  ```shell
  sudo pip3 install yapf
  sudo apt install pylint
  ```

- npm
  - config-conventional

    ```shell
    sudo apt install npm

    npm install --save-dev @commitlint/config-conventional @commitlint/cli
    npm install husky --save-dev
    commitizen init git-cz --save-dev --save-exact
    ```

## 联系

- Eric Liu @ Key R&D personnel
  - QQ: 3130676972
  - Github: [https://github.com/EricChoLiu/](https://github.com/EricChoLiu)
  - Gitee: [https://gitee.com/c12h22o11](https://gitee.com/c12h22o11)
  - Email: [ericcholiu@hotmail.com](ericcholiu@hotmail.com)

- AGVSC
  - Github: [https://github.com/AGVSC](https://github.com/AGVSC)
  - Gitee: [https://gitee.com/agvsc](https://gitee.com/agvsc)
