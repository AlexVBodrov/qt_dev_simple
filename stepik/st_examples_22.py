capitals = {'Россия': 'Москва', 'Англия': 'Лондон', 'Чехия': 'Прага', 'Бразилия':'Бразилиа'}

# for key, value in sorted(capitals.items(), key = lambda x: x[1]):
#     print(value)

# for value in sorted(capitals.values()):
#     print(value)


info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

print(info.get(['emp1']['name']))
print(info['emp2']['job'])
    