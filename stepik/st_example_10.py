def pretty_print(data, side='-', delimiter='|'):

    str_delimiter = f' {delimiter} '
    str_whith_delimiter = str_delimiter.join(map(str, data))
    midle_str = f"{delimiter} {str_whith_delimiter} {delimiter}"

    lenth_side = len(midle_str) - 2
    side_str = f" {side * lenth_side} "
    # print(len(side_str))
    # print(lenth_side)
    print(side_str)
    print(midle_str)
    print(side_str)


    

pretty_print(['abc', 'def', 'ghi', '12345'])