
import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None
mousePosition = pyautogui.position()

if ((len(sys.argv) < 2) or sys.argv[1].isalpha() or int(sys.argv[1]) < 1):
    numMin = 3
else:
    numMin = int(sys.argv[1])
print("Movement will be made every", numMin, "minutes")
while(True):
    x = 0
    move = True
    while(x < numMin):
        for i in range(0, 2):
            time.sleep(30)
            if pyautogui.position() != mousePosition:
                mousePosition = pyautogui.position()
                i = 0
                move = False
            else:
                move = True
        x += 1
    if(move):
        for i in range(0, 50):
            pyautogui.moveTo(0, i*4)
        pyautogui.moveTo(1, 1)
    for i in range(0, 3):
        pyautogui.press("shift")
    print("Movement made at {}".format(datetime.now().time()))
