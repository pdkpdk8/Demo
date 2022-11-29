import os
import random

# def get_screenshot():
#     # 截取手机的屏幕
#     os.system('adb shell /system/bin/screencap -p /sdcard/screencap.png')
#     # 把模拟器里面的文件或文件夹传到电脑上
#     os.system('adb pull /sdcard/screencap.png screencap.png')

adb_path = r"C:\Users\panmla\AppData\Local\Android\Sdk\platform-tools\adb.exe"
def jump(distance):
    # 设置按压时间,系数为1.35
    press_time = int(distance * 1.35)

    # 生成随机手机屏幕模拟触摸点,防止成绩无效
    # 生成随机整数(0-9),最终数值为(0-90)
    rand = random.randint(0, 9) * 10

    # adb长按操作,即在手机屏幕上((320-410),(410-500))坐标处长按press_time毫秒
    cmd = ("\""+adb_path+"\""+' shell input swipe %i %i %i %i ' + str(press_time)) % (320 + rand, 410 + rand, 320 + rand, 410 + rand)

    # 输出adb命令
    print(cmd)

    # 执行adb命令
    os.system(cmd)
jump(1000)
