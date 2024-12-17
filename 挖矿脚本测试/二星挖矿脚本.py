#切记使用皮卡堂微端登录
#不要移动窗口位置哦！！

import pygetwindow as gw
import pyautogui
import random
import time
import keyboard

# 禁用 fail-safe
pyautogui.FAILSAFE = False

# 查找窗口名称为 '4399皮卡堂' 的窗口
windows = gw.getWindowsWithTitle('4399皮卡堂')

if windows:
    # 获取第一个找到的窗口
    target_window = windows[0]

    # 激活窗口，使其置于前台
    target_window.activate()

    # 确保窗口激活后有足够的时间
    time.sleep(1)

    # 获取窗口的坐标和大小
    left, top, width, height = target_window.left, target_window.top, target_window.width, target_window.height
    print(f"窗口位置：({left}, {top}), 宽度：{width}, 高度：{height}")

    # 移动到地图页面+打开地图
    pyautogui.moveTo(left + 1368, top + 765)  # 调整为相对窗口的位置
    pyautogui.click()
    # 公共场景+选择矿洞
    pyautogui.click(left + 978, top + 337)  # 相对窗口的坐标
    pyautogui.click(left + 936, top + 367)  # 相对窗口的坐标
    pyautogui.click(left + 959, top + 529)  # 相对窗口的坐标
    pyautogui.click(left + 1102, top + 529)  # 相对窗口的坐标
    pyautogui.click(left + 1212, top + 308)  # 相对窗口的坐标

    # 给定的四个边界点
    points = [(728, 559), (1021, 410), (1326, 566), (1026, 702)]

    # 计算矩形的边界：最小 x, 最大 x, 最小 y, 最大 y
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    # 记录每个位置上次点击的时间
    last_click_time = {}

    # 记录特殊位置的上次点击时间
    last_special_click_time = 0

    # 定义一个退出标志
    exit_flag = False

    # 监听快捷键，按下 'Esc' 时退出脚本
    def on_esc_pressed():
        global exit_flag  # 使用 global 来修改全局变量 exit_flag
        exit_flag = True
        print("检测到 'Esc' 键，退出脚本...")

    # 注册快捷键
    keyboard.add_hotkey('Esc', on_esc_pressed)

    # 主循环，监听快捷键
    while not exit_flag:
        # 随机生成点击位置
        random_x = random.randint(min_x, max_x)
        random_y = random.randint(min_y, max_y)

        # 当前时间
        current_time = time.time()

        # 检查当前位置是否有历史记录
        position_key = (random_x, random_y)
        if position_key in last_click_time:
            time_diff = current_time - last_click_time[position_key]
            if time_diff >= 2:  # 如果在同一个位置点击超过 2 秒
                print(f"在同一位置点击超过 2 秒，执行特殊操作，点击 ({left + 965}, {top + 552})")
                pyautogui.click(left + 965, top + 552)  # 点击特殊位置
                time.sleep(1)  # 等待 1 秒以模拟执行操作
                print("继续挖矿...")

        # 记录当前点击位置的时间
        last_click_time[position_key] = current_time

        # 输出随机点击的坐标
        print(f"随机点击位置: ({random_x}, {random_y})")

        # 模拟鼠标移动到随机位置并点击
        pyautogui.click(left + random_x, top + random_y)  # 相对窗口坐标
        time.sleep(0.5)
        pyautogui.click(left + random_x, top + random_y)  # 相对窗口坐标

        # 检查是否到达特殊位置点击的时间
        if current_time - last_special_click_time >= 5:  # 每隔 5 秒点击一次特殊位置
            time.sleep(1)
            print("每隔 5 秒点击特殊位置")

            pyautogui.click(left + 965, top + 552)  # 点击特殊位置
            last_special_click_time = current_time  # 更新最后点击的时间

else:
    print("未找到 '4399皮卡堂' 窗口")
