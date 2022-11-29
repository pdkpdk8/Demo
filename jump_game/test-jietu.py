import os
from time import sleep
import cv2

adb_path = r"C:\Users\panmla\AppData\Local\Android\Sdk\platform-tools\adb.exe"
device_address = r"9987dd5f"
screenshot_path = r"game.png"

def screenshot(path = None):
	
	if(path != None):
		os.system("\""+adb_path+"\""+" -s "+device_address+" exec-out screencap -p > " + path)
	else:
		os.system("\""+adb_path+"\""+" -s "+device_address+" exec-out screencap -p > " + screenshot_path)
	
	sleep(0.5)

screenshot()
# def muban():
#     screenshot()
#     target = cv2.imread('screenshot_path')
#     for i in range(0,16):
#         templates = []
#         templates.append(r"F:\python\羊了个羊\Yang_Scripts\template_images\level_{}_aim_{}_{}.png".format(2,i,i+1))
