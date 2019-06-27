import base64
def sum_ss_2(chisl_2, leng):
    '''
    Выполняет сложение заданного числа в 2-чной СС к +1
    '''
    N = -1
    while chisl_2[N] != '0':
            N-=1
    #print(N)
    #print(chisl_2[:N]+'1')
    new_chisl = chisl_2[:N]+'1' + '0'*(abs(N)-1)
    return '0'*(leng-len(new_chisl)) + new_chisl

def create_table_ss16_ss2():
    '''
    Создает таблицу преобразования из 16-ой системы счисления в 2-ую системы счисления
    '''
    table_ss2 = {}
    massiv_synbols = [str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
    N = 4 
    last = '0'*N
    #print(last)
    for new_symbol in massiv_synbols:
        table_ss2[new_symbol] = last
        if last != '1'*N:
            last = sum_ss_2(last,N)
        #print(last)
    return table_ss2

def create_back_table_ss16_ss2():
    '''
    Создает таблицу преобразования из 2-ой системы счисления в 16-ую системы счисления
    '''
    table_ss2 = {}
    massiv_synbols = [str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
    N = 4 
    last = '0'*N
    #print(last)
    for new_symbol in massiv_synbols:
        table_ss2[last] = new_symbol
        if last != '1'*N:
            last = sum_ss_2(last,N)
        #print(last)
    return table_ss2

def symbol_to_ss2(symbol):
    '''
    Перевод 1-ого символа 16-ричной СС в 2-чную СС
    '''
    symbol = symbol.lower()
    ss_2 = create_table_ss16_ss2()
    if ss_2.get(symbol) == None:
        return  'Ошибка!'
    else:
        return ss_2[symbol]
    
def symbol_ss2_to_ss16(symbol):
    '''
    Перевод 1-ого символа 2-ричной СС в 16-чную СС
    '''
    symbol = symbol.lower()
    ss_2 = create_back_table_ss16_ss2()
    if ss_2.get(symbol) == None:
        return  'Ошибка!'
    else:
        return ss_2[symbol]
    
def ss2_to_ss16(stroka):
    s_new = ''
    N = 0
    for shag in range(len(stroka)//4):
        s_new += symbol_ss2_to_ss16(stroka[N:N+4])
        N += 4
    return s_new
    
    
def stroka_to_ss2(stroka):
    '''
    Перевод строки и каждого ее символа 16-ричной СС в 2-чную СС
    '''
    s_new = ''
    for x in stroka:
        s_new += symbol_to_ss2(x)
    return s_new

def XOR(buff_1,buff_2):
    sum_buff = ''
    L = len(buff_1)
    for x in range(L):
        if buff_1[x] != buff_2[x]:
            sum_buff += '1'
        else:
            sum_buff += '0'
    return  sum_buff

def XOR_ss16(buff_1,buff_2):
    '''
    XOR двух 16-ричных строк или буферов
    '''
    buff_1 = stroka_to_ss2(buff_1.lower())
    buff_2 = stroka_to_ss2(buff_2.lower())
    #print(buff_1)
    #print(len(buff_1))
    #print('-'*100)
    #print(buff_2)
    #print(len(buff_2))
    #print('-'*100)
    return ss2_to_ss16(XOR(buff_1,buff_2))


def create_table_base64():
    '''
    Создает таблицу преобразования из 2-ой системы счисления в base64
    '''
    base_64 = {}
    N = 6
    m_a = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)] + [str(x) for x in range(10)] + [chr(43)] +[chr(47)]
    #print(m_a)
    last = '000000'
    for x in m_a[:-1]:
        #print(last)
        base_64[last] = x
        last = sum_ss_2(last,N)
        #print(x,' : ',base_64[last])
    return base_64

def create_back_table_base64():
    '''
    Создает таблицу преобразования из base64 в 2-ой системы счисления
    '''
    base_64 = {}
    N = 6
    m_a = [chr(x) for x in range(65,91)] + [chr(x) for x in range(97,123)] + [str(x) for x in range(10)] + [chr(43)] +[chr(47)]
    #print(m_a)
    last = '000000'
    for x in m_a:
        #print(last)
        base_64[x] = last
        if last != '1'*N:
            last = sum_ss_2(last,N)
        #print(x,' : ',base_64[last])
    return base_64

def symbol_to_base64(symbol):
    '''
    Преобразование символа в 2-ой системы счисления в base64
    '''
    ss_base64 = create_table_base64()
    if ss_2.get(symbol) == None:
        return  'Ошибка!'
    else:
        return ss_2[symbol]
    
def stroka_to_base64(stroka):
    '''
    Преобразование строки в 16-ой системы счисления в base64
    '''
    ss_base64 = create_table_base64()
    s_new = stroka_to_ss2(stroka)
    N = 0
    s_n = ''
    for x in range(len(s_new) // 6 + 1):
        hex_l = s_new[N:N+6]
        #print(hex_l)
        if hex_l != '':
            if len(hex_l) != 6 :
                hex_l += '0'*(6 - len(hex_l))
            if ss_base64.get(hex_l) == None:
                #print('Ошибка!')
                s_n +=' '
            else:
                s_n += ss_base64[hex_l]
        #print(hex_l)
        N += 6
    return s_n

def ss2_to_base64(stroka):
    '''
    Преобразование строки в 2-ой системы счисления в base64
    '''
    ss_base64 = create_table_base64()
    N = 0
    s_n = ''
    for x in range(len(stroka) // 6 + 1):
        hex_l = stroka[N:N+6]
        #print(hex_l)
        if hex_l != '':
            if len(hex_l) != 6 :
                hex_l += '0'*(6 - len(hex_l))
            if ss_base64.get(hex_l) == None:
                #print('Ошибка!')
                s_n +=' '
            else:
                s_n += ss_base64[hex_l]
        #print(hex_l)
        N += 6
    return s_n

def base64_to_ss2(stroka):
    '''
    Преобразование строки base64 в 2-ну систему счисления
    '''
    ss_base64 = create_back_table_base64()
    ss2_new = ''
    for symbol in stroka:
        if ss_base64.get(symbol) == None:
            ss2_new += 'Ошибка!'
        else:
            ss2_new += ss_base64[symbol]
    return ss2_new

def zap(spis_b, x):#запись всех символов и количества их встреч в словарь
    #print(x)
    if spis_b.get(x) == None:
        spis_b[x] = 1
    else:
        spis_b[x] += 1
    #return spis_b
        
def chistot_symbols(input_):#парсим строку и складываем ее в словарь
    import operator
    spis_b = {}
    n = 2
    [zap(spis_b,x) for x in [input_[i - n:i] for i in range(n, len(input_) + 1, n)]]
    return sorted(spis_b.items(), key=operator.itemgetter(1), reverse = True)#сортируем словарь по значениям  


def decode_stroka(input_):
    chistot_symbol = chistot_symbols(input_)[:5]
    f_decode = True
    start = 0
    shag = 1
    while f_decode:
        symbol = XOR(stroka_to_ss2(str(chistot_symbol[start][0])),stroka_to_ss2('20'))
        #print('0',str(chistot_symbol[start][0]))
        #print('0',symbol)
        shifr_str = ss2_to_ss16(XOR(stroka_to_ss2(input_),symbol*(len(input_)//2)))
        try:
            symbol = bytes.fromhex(ss2_to_ss16(symbol)).decode()
            #print(shifr_str)
            shifr_str = bytes.fromhex(shifr_str).decode()
            #print('1',shifr_str)
            f_decode = False
            return symbol, shifr_str
        except Exception as e:
            pass
        if start >= len(chistot_symbol): f_decode = False
    return 'Неудалось расшифровать текст'

def shifr_duplicate_key(data,key):
    answer = ""
    lkey = len(key)
    #print(key)
    #print(lkey)
    for i in range(0, len(data), lkey):
        substr = data[i:i+lkey]
        #print('substr',substr)
        for l,k in zip(substr, key):
            #print('l',l)
            #print('k',k)
            #print('answer',answer)
            answer += chr(ord(l) ^ ord(k))
            #print('answer',answer)
    return bytes.hex(answer.encode())