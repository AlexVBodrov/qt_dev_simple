"""

1) Создаем список с неправильными словами
2) Создаем строку с файла с текстом
3) Создаем .lower() версию верхней переменной 
4) Пробегаемся циклом по списку неправильных слов и заменяем реплейсом s = s_lower.replace(i, '*'*len(i))
5) Создаем переменную fin = '' куда будем всё добавлять

6) Пробегаемся по длине строки s_lower и сравниваем её с изначальной строкой s. Если s_lower[i] == '*', добавляем звездочку, иначе если s_lower[i] != '*' and s_lower[i] != s[i], добавляем s[i]. В остальных случаяъ - s_lower[i]
7) Выводим результат
"""
name =input()

forbidden_words_lst = []

with open('forbidden_words.txt', 'r', encoding='utf-8') as forbidden_words_file:
    for w in forbidden_words_file.read().split():
        forbidden_words_lst.append(w)

with open(name, 'r', encoding='utf-8') as file:
    text = file.read()

import re
forbidden_words = forbidden_words_lst
my_string = text

def change(forbidden_words,text):
	out = text
	for w in forbidden_words:
		out = re.sub(w,"*"*len(w),out,flags=re.I|re.M)
	return out
print(change(forbidden_words,my_string))