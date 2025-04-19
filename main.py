import pyautogui
import time
import random

while True:
    x = random.randint(100,600)
    y = random.randint(600,800)
    time.sleep(2)
    pyautogui.moveTo(x,y)
