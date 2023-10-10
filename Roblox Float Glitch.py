import win32gui
import win32api
import win32con
import keyboard

win2find = "Roblox"

class Freeze():
    def __init__(self) -> None:
        self.canPress = True
    
    def click(self, x, y):
        hWnd = win32gui.FindWindow(None, win2find)
        lParam = win32api.MAKELONG(x, y)

        hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
        win32gui.SendMessage(hWnd1, win32con.WM_RBUTTONDOWN, win32con.MK_RBUTTON, lParam)
        win32gui.SendMessage(hWnd1, win32con.WM_RBUTTONUP, None, lParam)


    def Freezer(self):
        if self.canPress:
            whnd = win32gui.FindWindowEx(None, None, None, win2find)
            if not (whnd == 0):
                print('Found')
                self.click(100,100)
            else:
                print('Roblox Not Opened')


keyboard.add_hotkey('y', Freeze().Freezer)

while True:
    keyboard.read_key()
