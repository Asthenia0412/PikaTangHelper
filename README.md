# PikaTangHelper
 皮卡堂自动化工具：

本项目持续更新。

## 1.圣诞节脚本-自动摆放圣诞袜

### A.需求分析：

圣诞节的袜子需要手动摆放到房间的墙壁上，这对人的精力是很大的挑战

我用Python的pyautogui来模拟鼠标的操作，实现自动摆放

![image-20241217202838440](./assets/image-20241217202838440.png)

### B.使用教程

> 在上图你需要使用全屏截图工具，确定若干坐标
>
> A.圣诞袜的坐标
>
> B.你要摆放的墙面的四个角的(x,y)

在确定完坐标后,将具体的坐标数值填入到代码注释部分即可

我推荐你采用分屏形式来执行脚本，如下图所示：

![image-20241217203054588](./assets/image-20241217203054588.png)

### C.后记

圣诞袜的获取：西广场处圣诞老人购买

圣诞袜的填充：每日12点自动刷新

## 2.挖矿脚本

### A.使用须知：

![image-20241218001126719](./assets/image-20241218001126719.png)

请使用皮卡堂微端登录：4399

默认的点位定位是基于默认的微端位置的

请开启脚本时不要点开任何的界面

请确保不要隐藏工具栏，确保右下方的地图是可以被点击的

### B.使用教程

运行python脚本会唤出游戏界面

退出脚本按下ESC即可

### C.特殊处理

矿洞情况比较复杂，本脚本仅仅处理了基本的矿洞升层问题：

考虑到识别图像比较复杂，我们直接定时5s点击一次确认升层。

