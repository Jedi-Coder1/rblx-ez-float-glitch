import win32gui
import win32api
import win32con
import keyboard

win2find = "Roblox"

def keyboardInput(typ):
    whnd = win32gui.FindWindowEx(None, None, None, win2find)
    if not (whnd == 0):
        print('Found')

while True:
    if keyboard.is_pressed('y'):
        print('Freezing')
        keyboardInput("Freeze")
    elif keyboard.is_pressed('u'):
        print('Unfrozen')
        keyboardInput("Unfreeze")
