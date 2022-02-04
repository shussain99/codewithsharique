import pyautogui
import time
pyautogui.FAILSAFE = False
k=1200
l=300
i=1
p=0
for i in range(10000000):
    time.sleep(25)
    pyautogui.moveTo(k, l, duration = 1)
    p=k
    k=l
    l=p
