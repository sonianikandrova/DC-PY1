def get_count_char(str_):
    dict = {}
    str_ = str_.lower()
    for k in str_:
        if k not in dict and k.isalpha():
            dict.setdefault(k, 1)
        else:
            if k in dict:
                dict[k]+=1
    return dict

def ratio(dict2):
    for k, value in dict2.items():
        dict2[k]=str(value*100/sum(dict2.values()))+"%"
    return dict2

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
