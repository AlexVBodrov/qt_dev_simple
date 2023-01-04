"""
Хороший пароль по условиям этой задачи состоит как минимум из 7 символов, 
содержит хотя бы одну цифру, 
заглавную 
и строчную букву. 
Напишите программу со встроенной функцией any() для определения хорош ли введенный пароль.
"""
# password = input("Enter password")

password = 'DFSDFSDFSDsdfjsdfnsm'


def is_lenth(password: str) -> bool:
    return len(password) >= 7

def is_num(password: str) -> bool:
    for el in password:
        if el.isdigit():
            return True
    return False

def is_low(password: str) -> bool:
    for el in password:
        if el.islower():
            return True
    return False

def is_upper(password: str) -> bool:
    for el in password:
        if el.isupper():
            return True
    return False

validate_password_tuple = is_lenth(password), is_num(password), is_low(password), is_upper(password)
print(validate_password_tuple)
is_validate = all(validate_password_tuple)
print(is_validate)

"""
s = input()
print('YES' if all((any(i.isupper() for i in s), 
                    any(i.islower() for i in s), 
                    any(i.isdigit() for i in s), 
                    len(s) >= 7)) else 'NO')
                    
"""