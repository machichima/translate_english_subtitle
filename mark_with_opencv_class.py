import cv2
import make_window_in_the_front
import os

#global img, clone
paint = 0
class mark():
    esc = 1
    def select(self):
        path = os.getcwd()
        mark.esc = 1
        pic = cv2.imread(path+'/data/pic_1.png')   #截圖畫面
        mask = cv2.imread(path+'/data/mask.png')   #全白圖片
        img = cv2.addWeighted(pic, 0.8, mask, 0.2, 1)   #創建mask，讓畫面變得像截圖畫面
        clone = img.copy()   #複製畫布

        def onMouse(event, x, y, flags, param):   #滑鼠事件
            global paint
            clone = img.copy()
            if(paint == 1):   #當按下左鍵後拖移時，矩形滑鼠走
                cv2.rectangle(clone, rec[0], (x, y), (0, 0, 0), 2)
                cv2.imshow('hi', clone)
                #scretch(x, y)
            if(event == cv2.EVENT_LBUTTONDOWN):   #按下左鍵
                print("(x, y) = (%d, %d)"%(x, y))
                rec.append((x, y))
                paint = 1
            elif(event == cv2.EVENT_LBUTTONUP):   #放開左鍵
                print("(x_1, y_1) = (%d, %d)"%(x, y))
                rec.append((x, y))
                print(rec)
                cv2.rectangle(clone, rec[0], rec[1], (0, 0, 0), 2)
                paint = 0
                cv2.imshow('hi', clone)
                while(1): 
                    #如果不放的話，把下面的keyin改成cv2.waitKey(0)
                    # 則第一個if要按1下，第二個if要按兩下，以此類推
                    keyin = cv2.waitKey(0)   
                    if(keyin == 27):   #當按下esc
                        #mark.esc = 1
                        print(mark.esc)
                        cv2.waitKey(1)
                        cv2.destroyAllWindows()
                        break
                    if(keyin == ord('s')):   #按下s鍵，擷取所選範圍
                        print("yes")
                        scretch(x, y)
                        cv2.waitKey(1)
                        cv2.destroyAllWindows()
                        break
                    if(keyin == ord('n')):  #按下n鍵，重新選取
                        del rec[:]
                        print("clear")
                        clone = img.copy()
                        cv2.imshow('hi', clone)
                        cv2.destroyWindow('img')
                        break
                print('out_def')

        def scretch(x, y):   #讓矩形能從任何方面框選
            if(y < rec[0][1]):
                img_1 = pic[y : rec[0][1] , rec[0][0] : x]
            elif(x < rec[0][0]):
                img_1 = pic[rec[0][1] : y, x : rec[0][0]]
            elif(y < rec[0][1] and x < rec[0][0]):
                img_1 = pic[y : rec[0][1], x : rec[0][0]]
            else:
                img_1 = pic[rec[0][1] : y, rec[0][0] : x]
            
            cv2.imwrite(path+'/data/word.png', img_1)   #儲存所框選區域
            mark.esc = 0
        
        cv2.namedWindow('hi', cv2.WINDOW_NORMAL)
        #設定視窗全螢幕
        cv2.setWindowProperty('hi', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        rec = []
        cv2.imshow('hi', img)
        make_window_in_the_front.front()   #使截圖畫面在最前面
        cv2.setMouseCallback('hi', onMouse)   #滑鼠事件
        print("pass")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if(__name__ == '__main__'):
    #esc = 1
    a = mark()
    print('*', mark.esc)
    a.select()


    