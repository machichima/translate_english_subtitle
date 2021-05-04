import os
def _ch(vol, p_o_s, ch, len_p, path):   #寫入中文解釋的txt檔
    #用硬來的方式排版
    name = open(os.getcwd()+'/data/store_place.txt')
    f = open(path + '/' + name.read().split('\n')[1],'a')
    s_1 = vol + '\n'
    s_2 = list()
    s = str()
    s_2.append('\t')
    for i in range(len_p):
        s_2.append(p_o_s[i] + '\n')
        print(len(ch[i]))
        for j in range(len(ch[i])):
            ch[i][j] = ch[i][j].replace('；', ' / ')
            s_2.append(ch[i][j] + '\n')
    for x in s_2:
        s = s + x
    s = s_1 + s + ';'
    f.write(s)
    f.close()

def _eng(vol, p_o_s, eng, len_p, path):   #寫入英文解釋的txt檔
    #用硬來的方式排版
    name = open(os.getcwd()+'/data/store_place.txt')
    f = open(path + '/' + name.read().split('\n')[2],'a')
    s_1 = vol + '\n'
    s_2 = list()
    s = str()
    s_2.append('\t')
    for i in range(len_p):
        s_2.append(p_o_s[i] + '\n')
        for j in range(len(eng[i])):
            s_2.append(eng[i][j] + '\n')
    for x in s_2:
        s = s + x
    s = s_1 + s + ';'
    f.write(s)
    f.close()

if(__name__ == '__main__'):
    vol = 'word'
    p_o_s = ['p_o_s']
    eng = ['eng']
    ch = ['ch']
    sentence = ['sentence']
    len_ch = 1
    quantity = 1
    _ch(vol, p_o_s, ch, sentence, len_ch)
    _eng(vol, p_o_s, eng, sentence, quantity)