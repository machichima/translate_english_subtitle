import requests
from bs4 import BeautifulSoup
import re

def p_o_s_func(translation):
    p_o_s_text = translation.find('span', attrs = {'class': 'pos dpos'}).text
    return p_o_s_text
    '''
    try:
        p_o_s_text = translation.find(attrs = {'class': 'dsense_h'}).text
        index, index_1 = p_o_s_text.index('('), p_o_s_text.index(')')
        #print(index, index_1)
        replace_text = p_o_s_text[:index].replace(' ', '').replace('\n', '') + p_o_s_text[index:index_1] + p_o_s_text[index_1:].replace(' ', '').replace('\n', '')
        return replace_text[len_word:] 
    except ValueError:
        p_o_s_text = translation.find(attrs = {'class': 'gram dgram'}).text
        return p_o_s_text
    except:
        pass
    '''
def eng_d_func(component):
    eng_text_1 = []
    for c in component:
        eng_text = c.find(attrs = {'class': 'def ddef_d db'}).text
        eng_text_1.append(eng_text)
    #print(eng_text)
    return eng_text_1 

def ch_d_func(component):
    ch_text_1 = []
    for c in component:
        try AttributeError:
            try AttributeError:
                ch_text = c.find(attrs = {'class': 'trans dtrans dtrans-se'}).text
            except:
                ch_text = c.find(attrs = {'class': 'trans dtrans dtrans-se'})
        except:
            try AttributeError:
                ch_text = c.find(attrs = {'class': 'trans dtrans dtrans-se break-cj'}).text
            except:
                ch_text = c.find(attrs = {'class': 'trans dtrans dtrans-se break-cj'})
        ch_text_1.append(ch_text)
        #print(ch_text)
    return ch_text_1

def sentence_func(component):
    sentence_1 = []
    for c in component:
        try:
            sentence = c.find(attrs = {'class': 'eg deg'}).text
            sentence_1.append(sentence)
        except:
            sentence_1.append(None)
    return sentence_1

def sentence_ch_func(component):
    sentence_ch_1 = []
    for c in component:
        try:
            sentence_ch = c.find(attrs = {'class': 'trans dtrans dtrans-se hdb'}).text
            sentence_ch_1.append(sentence_ch)
        except:
            sentence_ch_1.append(None)
    return sentence_ch_1

def translate(word):    
#word = 'deceive'   #device
    url = 'https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/{}'.format(word)
    print(url)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    headers = {
                    'User-Agent': user_agent
                }
    html = requests.get(url = url, headers = headers).content
    sp = BeautifulSoup(html, 'html.parser')
    #print(sp.find('div', {'bpb c_ps lmb-25 lp-20 lpt-25 lp-s_l-25'}))
    if(sp.find('div', {'bpb c_ps lmb-25 lp-20 lpt-25 lp-s_l-25'}) == None):
        try:
            word = sp.find('span', {'class': 'headword'}).getText()
        except ValueError:
            word = sp.find('h2', {'class': 'headword'}).getText()
        len_word = len(word)    
        print(word)
        translation_all = sp.find_all(attrs = {'class': 'pr entry-body__el'})
        '''
        if(sp.find_all(attrs = {'class': 'pr dsense'}) != []):
            translation_all = sp.find_all(attrs = {'class': 'pr dsense'})
        else:
            translation_all = sp.find_all(attrs = {'class': 'pr dsense dsense-noh'})#pr dsense
        '''
        #print(translation_all)
        p_o_s, eng_d, ch_d, sentence, sentence_ch = list(), list(), list(), list(), list()
        #print(len(translation_all))
        for translation in translation_all:
            #print(translation)
            p_o_s.append(p_o_s_func(translation))
            component = translation.find_all('div', {'class': 'def-block ddef_block'})
            print(len(component))
            print(component)

            eng_d.append(eng_d_func(component))
            ch_d.append(ch_d_func(component))
            sentence.append(sentence_func(component))
            sentence_ch.append(sentence_ch_func(component))
        #print(p_o_s)
        print(p_o_s, eng_d, ch_d, sentence, sentence_ch, sep = '\n')
        
        return word, p_o_s, eng_d, ch_d, sentence, sentence_ch
    else:
        print('no')
        return None, None, None, None, None, None

if __name__ == '__main__':
    translate('ok')