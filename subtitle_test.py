import pytesseract
from PIL import Image
import os

def get():   #選取區域轉換為文字
    path = os.getcwd()
    img = Image.open(path+'/data/word.png')
    #img.show()
    word = pytesseract.image_to_string(img, lang="eng")
    #print(word)
    return word
