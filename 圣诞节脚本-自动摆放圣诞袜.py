import pyautogui
import random
import time

# 移动鼠标到指定坐标
# 抓取圣诞袜
while True:
    #这是你背包中圣诞袜的坐标
    #获取方式：你可以用QQ的全屏截图，截取在该区域下圣诞袜的尾椎
    pyautogui.moveTo(562, 679, duration=0)  # 立即移动到指定位置

    # 鼠标左键按下
    pyautogui.mouseDown()

    # 生成一个随机的目标位置 (x, y)
    # 注意：这个位置是你的圣诞袜要拖拽到的墙面
    # 由于皮卡堂的房间墙壁是三维坐标系，并不好表达定量表达
    # 我们采取随机量的方式
    # 你可以选取要贴的墙面的四个顶点的x y值填入下面的框内
    random_x = random.randint(500, 940)
    random_y = random.randint(300, 570)

    # 移动鼠标到随机坐标，减少时间延迟，加速移动
    #切记：一定不能改变+1的随机行，因为皮卡堂对家具从背包拖拽摆放的判定是：要移动一个像素才能实现
    pyautogui.moveTo(random_x, random_y, duration=0)  # 立即移动到随机位置
    pyautogui.moveTo(random_x + 1, random_y + 1, duration=0)  # 稍微调整一下位置

    # 鼠标左键松开
    #这里是完成摆放
    pyautogui.mouseUp()
