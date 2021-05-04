import do_screenshot
import subtitle_test as subtitle
import mark_with_opencv_class
import scretch_cambridge as scretch
import GUI
import save
import save_in_excel as excel
import os

def sep_eng(eng_1):   #將一段英文解釋以每行大約為50字來分段
    a = []
    for e in eng_1:
        for j in range(len(e)):
            temp = e[j].split()
            sum = 0 
            for i in range(len(temp)):
                sum += len(temp[i])
                if(sum > 60):
                    print(sum)
                    temp[i] = '\n' + temp[i]
                    sum = 0
            e[j] = ' '. join(temp)
        #eng_1[j] = ' '. join(temp)   用這個的話好像會改到原始值
        #print('**************************************')
    #print(eng)
    return eng_1#eng_1

def sep_sentence(sentence):   #將一段句子以每行大約為60字來分段
    a = []
    for s in sentence:
        for j in range(len(s)):
            try:
                temp = s[j].split()
                sum = 0 
                for i in range(len(temp)):
                    sum += len(temp[i])
                    if(sum > 60):
                        temp[i] = '\n' + temp[i]
                        sum = 0
                s[j] = ' '. join(temp)
            except AttributeError:
                s[j] = None
        #sentence[j] = ' '. join(temp)
    #print(sentence) 
    return sentence#sentence

f = open(os.getcwd()+'/data/store_place.txt')   #取得store_place.txt中的資料
path = f.read().split('\n')[0]   #取得store_place.txt中的存取位置
path = '/'.join(path.split('\\'))   #python 不支援'\'，所以將其改成'/'
print(path)

p_o_s_change = {'名詞':'(n.)', '動詞':'(v.)', '形容詞':'(adj.)', '副詞':'(adv.)', '代名詞':'(pron.)', 
            '介系詞':'(prep.)', '感歎詞':'(int.)', '連接詞':'(conj.)'
        }   #爬蟲爬下來詞性為中文，將其以字典轉為英文
while(1):
    esc = 0   #是否按下esc鍵 
    do_screenshot.run()   #截圖
    a = mark_with_opencv_class.mark()   
    a.select()   #選取區域；esc為確認是否在框選期間關閉視窗
    if(not a.esc):
        word = subtitle.get()   #用tesseract將所選擇區域中的字提取出來
        print('*', word)
        cond, check = GUI.window_check(word)   #確認用視窗
        if(cond != None):   #沒有關閉確認視窗
            if(check[0] != ''):   #如果輸入框有輸入東西，則取輸入的東西
                word = check[0]
                print(word)
            #vol, ch_d, eng_d = web_crawler.translate(word.lower())   #爬取資料
            vol, p_o_s, eng_d, ch_d, sentence, sentence_ch = scretch.translate(word.lower())

            if(vol != None):
                try:  
                    eng = sep_eng(eng_d)   #將一段英文解釋以一定字數換行
                except:
                    eng = None
                try:
                    sentence_1 = sep_sentence(sentence)   #將一段句子以一定字數換行
                except:
                    sentence_1 = None
                try:
                    sentence_ch_1 = sep_sentence(sentence_ch)
                except:
                    sentence_ch_1 = None
                #顯示頁面
                event = GUI.windows(vol, p_o_s, eng, ch_d, sentence_1, sentence_ch_1, len(p_o_s)) 
                print(event)
                for e in event:   #儲存資料
                    if(e == 'to_ch'):   #存到中文txt檔
                        save._ch(vol, p_o_s, ch_d, len(p_o_s), path)   #
                    if(e == 'to_eng'):   #存到英文txt檔
                        save._eng(vol, p_o_s, eng, len(p_o_s), path)
                    if(e == 'to_excel'):   #存到excel
                        excel.save(vol, p_o_s, eng, ch_d, sentence_1, sentence_ch_1, len(p_o_s), path)
            else:
                GUI.windows_None()   #顯示no result! 頁面