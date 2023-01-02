my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def my_map(function, sequence):
    result = []
    for el in sequence:
        result.append(function(el))
    return result

def multi_2(item):
    return item * 2

def mult(x, y):
    return x*y


def my_odd(item):
    if item % 2 ==0:
        return True

def my_no_odd(item):
    return item % 2


def my_filter(function, sequence):
    result = []
    for el in sequence:
        if function(el):
            result.append(el)
    return result

def my_reduce(function, sequence, initial_value):
    accumulator = initial_value
    for el in sequence:
        accumulator = function(accumulator, el)
    return accumulator


if __name__ == '__main__':
    # print(my_map(multi_2, my_list))
    # print(my_filter(my_odd, my_list))
    # print(my_filter(my_no_odd, my_list))
    # print(my_reduce(mult, my_list, 1))
    # words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'deified', 'bbbbb', 'mother', 'surface', 'sister']

    # words_len = map(len, words)
    # print(max(words_len))
    # def predicate(word):
    #     return word == word[::-1]


    # words = ['abba', 'qwerty', 'python', 'a', 'deed', 'nun', 'level', 'language', 'deified', 'bbbbb', 'mother', 'sister', 'surface', '1234321']
    # filtered = my_filter(predicate, words)
    # print(filtered)
    # print(len(filtered))
    # numbers = [-2, 45, 45, -7, -45, 37, -42, 27, -58, -58, -12, -27, -49, -27, -56, 4, -99, -11, 86]

    # var1 = max(numbers, key=abs)
    # print(var1)
    # var2 = min(map(abs, numbers))

    # print(var1 + var2)
    # numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
    # # num = 
    # filter_numbers = my_filter((lambda x: len(str(x)) == 3 and x % 5 == 2), numbers)
    # print(filter_numbers)
    # res = my_map((lambda x: x**3), filter_numbers)
    # print(res)
