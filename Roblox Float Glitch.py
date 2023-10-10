import win32gui
import win32api
import win32con
import keyboard

win2find = "Roblox"

def keyboardInput():
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        print('Found')
