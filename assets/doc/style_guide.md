# Style Guide


## 仓库

### 命名格式

`agv-${REPONAME}`，全小写，单词间`-`连接，以`agv-`开头

### 导入仓库设置

提供了Template作为模板仓库用于快捷导入

## C++

### 参考`Google Style C++ Guide`

- 与`Google Style C++ Guide`冲突的内容以本文当为先
- 关于本文档未描述的内容参考`Google Style C++ Guide`
  - [中文版](https://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/contents/)
  - [英文版](https://google.github.io/styleguide/cppguide.html)
*third_party内文件和其余SDK文件不需要依据本文档进行编码*

### C++版本

`C++11`/`C++17` 为主，在版本不兼容情况下可以使用其他标准

### 库结构

| 文件夹名 | 注释 |
|:------ | :--- |
| *essential* | |
| build | 编译产生的中间文件 |
| include | 头文件 |
| lib | `.a` `.so` `.dll` `.lib` 库文件 |
| src | 源文件 |
| *optional* | |
| assets *`optional`* | 资源，如图片等 |
| assets/doc *`optional`* | 文档 |
| assets/image *`optional`* | 图片 |
| app *`optional`* | 生成的应用程序 |
| third_party *`optional`* | 第三方库 |
| utils *`optional`* | `.sh`和`.py`等脚本文件 |
| *ROS* | |
| cfg *`optional`* *`ROS`* | `.cfg`文件 |
| launch *`optional`* *`ROS`* | `.launch`文件  |
| msg *`optional`* *`ROS`* | `.msg`文件 |
| rviz *`optional`* *`ROS`* | `.srv` 文件|
| scripts *`optional`* *`ROS`* | `rospy` 脚本文件 |
| srv *`optional`* *`ROS`* | `.srv`文件 |

### Header

### 头文件后缀

使用`.hpp`作为后缀

- *必要时使用`.h`*

### 头文件标点格式

`<>`:用于标准库文件
`""`:自定义的头文件，ROS库、第三方库内其他文件

### 头文件顺序

```C++
// C++标准库
#include <iostream>
// C标准库
#include <stdio.h>
// Boost
#include "boost/boost.hpp"
// ROS
#include "ros/ros.h"
// 第三方依赖
#include "opencv/opencv.hpp"
// 项目内文件
#include "include/header.hpp"
```

### 头文件保护

- （不建议）使用`#pragma once`进行守护

- （建议）  按照`#ifndef #define #endif`进行保护，且符号名称应为`__<PROJECT>_<FILENAME>_HPP__`

例如`agv-hik-cam/include/sdk/net_sdk.hpp`，有如下格式

```C++
#ifndef __AGV_HIK_CAM_NET_SDK_HPP__
#define __AGV_HIK_CAM_NET_SDK_HPP__
...
#endif // __AGV_HIK_CAM_NET_SDK_HPP__

// or

#pragma once
```

### Source

### 源文件后缀

使用`.cpp`作为后缀

- *必要时使用`.cc`*

### 命名规范

#### 变量命名

##### 一般变量

- 使用向全小写和下划线组合的方式，如`temp_var`
- 常见的缩略词首字母大写，其余均小写，如`var_Usb`

##### const

在一般变量前加`k`,如`k_temp_var`

##### 类内变量

一般变量后加下划线，如`temp_var_`

##### 结构体变量

与一般变量名一致

##### enum变量

k开头全大写加下划线

#### 文件名命名

与一般变量名一致

#### 类命名

- 大驼峰命名法
- 是ROS类则在后面加上`_ROS`
- 常见的缩略词首字母大写，其余均小写，如`Usb`

#### 函数命名

- 大驼峰命名法
- 常见的缩略词首字母大写，其余均小写，如`FindUsb`

#### 宏命名

全大写和下划线

#### 作用域

##### namespace

- （鼓励）使用`namespace`嵌套
- 不使用缩略名

## markdown

- 遵循markdownlint的审查准则，不允许

## 准则

不鼓励不按本编码风格规范的代码提交
不接受不按本编码风格规范的commit合并
