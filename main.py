# -*- coding: utf-8 -*-

import pyautogui
import time
import random

def warptoyellowstargate():
    #pyautogui.typewrite('Hello world! ',0.2)
    #pyautogui.press('right')
    #for folder_location in pyautogui.locateAllOnScreen('D:/foldericon.png'):
    pyautogui.moveTo(960,540)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    iconlocation = pyautogui.locateOnScreen('D:/waypointicon.png')
    print(iconlocation)
    if(iconlocation):
        iconx,icony = pyautogui.center(iconlocation)
        pyautogui.moveTo(iconx,icony)
        pyautogui.click()
        pyautogui.press('d')
        time.sleep(10+5*random.random())
        pyautogui.press('d')
        #pyautogui.hotkey('alt','f1')

def main():
    while(1):
        warptoyellowstargate()
        time.sleep(5+5*random.random())

if __name__ == '__main__':
    main()
