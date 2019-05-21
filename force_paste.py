#This programs force pastes things if for some reason you cannot paste regularly (eg typying your email twice when siging up for a website)
#I call this program by cmd+ctrl+v
import pyautogui, pyperclip
pyautogui.typewrite(pyperclip.paste())
