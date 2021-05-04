import pyautogui, pynput
import mark_with_opencv
import os
def run():
    path = os.getcwd()
    def on_press(key):
        try:
            if(key == pynput.keyboard.Key.alt_l):     
                listener.stop()   #停止鍵盤監聽
                img = pyautogui.screenshot()   #截圖
                img.save(path+'/data/pic_1.png')
        except AttributeError:
            pass
    with pynput.keyboard.Listener(on_press = on_press) as listener:
        listener.join()

if(__name__ == '__main__'):
    run()