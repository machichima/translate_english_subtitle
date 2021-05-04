import PySimpleGUI as sg
sg.theme('LightGrey')

def windows_None():   #沒有查詢到資料時顯示的視窗
    layout = [[sg.Text('no result!', font = ("Gungsuh", 12))]]
    sg.theme_background_color('white')
    window = sg.Window('None', layout)
    window.Read()
    window.Close()

def window_check(vol):   #確認用視窗
    layout = [
            [sg.Text('這是你要的字嗎?', size = (0, 0), font = ("Gungsuh", 12))],
            [sg.Text(vol, size = (0, 0), font = ("Gungsuh", 12))],
            [sg.Text('如果不是，請輸入你要查詢的單字:', size = (0, 0), font = ("Gungsuh", 12))],
            [sg.Input(size=(12, 1), background_color='Gray')],
            [sg.OK()],
            ]
    window = sg.Window('check', layout)
    event, value = window.Read()
    window.Close()
    return event, value
    
def sentence_length(sentence):
    if(sentence != None):
        return [[sg.Text(sentence, font = ("Gungsuh", 15))],
                [sg.Text('-------------------------------------------------------')]]
    else:
        return [[sg.Text('-------------------------------------------------------')]]

#形成GUI頁面
def make_windows(start, length, vol, p_o_s, eng, ch, sentence, sentence_ch, len_eng):
    start_page = start + 1
    layout_1 = [[sg.Text(vol, size = (0, 0), font = ("Gungsuh", 35)),
                 sg.Button('save in\nch', key = 'to_ch', size = (6, 2)),
                 sg.Button('save in\neng', key = 'to_eng', size = (6, 2)),
                 sg.Button('save to\nexcel', key = 'to_excel', size = (6, 2)),
                 sg.Button('<-', key = 'last_page', size = (6, 2)),
                 sg.Button('->', key = 'next_page', size = (6, 2)),
                 sg.Text(str(start_page) + '/' + str(len(eng)), size = (0, 0), font = ("Gungsuh", 10))
                 ]]
    layout_2 = []
    for i in range(start, length):
        #此時中文和英文解釋都還有
        arr = [
            [sg.Text(p_o_s[i], font = ("Gungsuh", 12))],
        ]

        arr_1 = []
        for j in range(len(eng[i])):
            arr_d = [
                [sg.Text(eng[i][j], font = ("Arial Unicode MS", 15), auto_size_text=True)],
                [sg.Text(ch[i][j], font = ("Arial Unicode MS", 15), text_color = '#0580e8')]           
            ]

            if(sentence[i][j] != None):
                arr_s = [
                    [sg.Text(sentence[i][j], font = ("Gungsuh", 15))],
                    [sg.Text(sentence_ch[i][j], font = ("Arial Unicode MS", 15), text_color = '#0580e8')],
                    [sg.Text(' ')]
                ]
            else:
                arr_s = [
                    [sg.Text(' ')]
                ]
            arr_1 = arr_1 + arr_d + arr_s
        arr = arr + arr_1
        layout_2 = layout_2 + arr

    layout = layout_1 + layout_2

    return layout

def windows(vol, p_o_s, eng, ch, sentence, sentence_ch, len_eng):   #顯示資訊的視窗
    x = 0
    more_then_one = 0
    if(len_eng > 1):
        more_then_one = 1
    else:
        more_then_one = 0

    layout = make_windows(0, 1, vol, p_o_s, eng, ch, sentence, sentence_ch, len_eng)
    
    sg.theme_background_color('white')#('white')
    loc = (600, 100)
    window = sg.Window('window', layout, location = loc, alpha_channel=0).Finalize()
    window.SetAlpha(1)
    size = window.Size
    e = []
    event, value = window.Read()   #讀取按鍵及是否再輸入框輸入值
    if(more_then_one == 1):
        while(event != None):
            if(event == 'next_page'):
                if(x < len_eng - 1):
                    x += 1
                    layout_2 = make_windows(x, x + 1, vol, p_o_s, eng, ch, sentence, sentence_ch, len_eng)
                    window_2 = sg.Window('window_2', layout_2, location = loc, alpha_channel=0).Finalize()
                    window_2.size = size
                    window_2.SetAlpha(1)
                    window.close()
                    window = window_2

            elif(event == 'last_page'):
                if(x > 0):
                    x -= 1
                    layout_2 = make_windows(x, x+1, vol, p_o_s, eng, ch, sentence, sentence_ch, len_eng)
                    window_2 = sg.Window('window_2', layout_2, location = loc, alpha_channel=0).Finalize()
                    window_2.size = size
                    window_2.SetAlpha(1)
                    window.close()
                    window = window_2
                else:
                    pass
            else:
                while(event != None):
                    e.append(event)
                    event, value = window.Read()
                    print('1')
                break
            event, value = window.Read()
    
    else:
        while(event != None):
            e.append(event)
            event, value = window.Read()
    return e
    window.close()
        
        
        
    #window.Read()

if(__name__ == '__main__'):
    vol = 'test'
    p_o_s = ['n.', 'v.', 'v.']
    eng = [['eng', 'eng'], ['eng', 'eng'], ['eng']]
    ch = [['中文', '中文'], ['中文', '中文'], ['中文']] 
    sentence = [[None, 'sentence_1'], ['sentence_1', 'sentence_1'], ['sentence_1']]
    sentence_ch = [[None, 'sentence_ch_2'], ['sentence_ch_2', 'sentence_ch_2'], ['sentence_ch_2']]
    quantity = 3
    a = window_check('vol')
    print(a)
    windows_None()
    print(windows(vol, p_o_s, eng, ch, sentence, sentence_ch, quantity))
    