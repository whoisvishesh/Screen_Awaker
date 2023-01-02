import pyautogui
import time 

pyautogui.FAILSAFE = False
while True:
    time.sleep(100)
    for i in range(0,200):
        pyautogui.moveTo(500 ,i*5)
    for i in range(0,3):
        pyautogui.press("Shift")
        exit()