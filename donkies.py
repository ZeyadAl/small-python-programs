'''
This program is made so you don't have to write your email (or anything) twice
while filling a form or even once
'''
import pyautogui as gui
import time
#x = input('Enter the x coordinates ')
#y = input('Enter the y coordinates ')

for i in range(250):
        #gui.click(x, y)
	time.sleep(2)
	gui.typewrite('hello omar')
