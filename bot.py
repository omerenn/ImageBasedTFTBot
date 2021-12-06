from pyautogui import *
import pyautogui as pag
import time as t
import win32api, win32con

t.sleep(5)
# Click Function: 
def clickFunc (image):
    var1, var2 = pag.locateCenterOnScreen(image, confidence=0.7)

    win32api.SetCursorPos((var1, var2))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    t.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Main Event
while True:
    clickFunc ("img/1.png")
# Checking for "Accept" button:       
    while True:
        while True:
            if pag.locateOnScreen("img/3.png", confidence = 0.7) != None:
                clickFunc("img/3.png")
                break

            else:
                continue


        t.sleep(15)
# Checking for someone rejected:
        if pag.locateOnScreen("img/2.png", confidence=0.7) == None:
            break
        else:
            continue
    
    t.sleep (25)
# Checking for still in loading screen:    
    while pag.locateOnScreen("img/0.png", confidence = 0.7):
        t.sleep(1)
    
    t.sleep(3)
# For surrender: 
    clickFunc("img/4.png")

    t.sleep(600)

    clickFunc("img/5.png")

    t.sleep(3)

    clickFunc("img/6.png")

    t.sleep(15)

    clickFunc("img/7.png")

    t.sleep(5)