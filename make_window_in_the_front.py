import win32gui, win32com.client

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def front():
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    #print(top_windows)
    for i in top_windows:
        if "hi" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.SetForegroundWindow(i[0])
            break
if __name__ == "__main__":
    front()