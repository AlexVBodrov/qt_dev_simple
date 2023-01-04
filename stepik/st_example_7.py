# 10.0.1.1 True
# 10.1.1.a False
ip = '10.0.1.000234'

is_4_length = lambda x: len(x.split('.')) == 4
is_0_255 = lambda x: 0 <= int(x) <= 255
result_list = list(map(lambda x: is_4_length(ip) and x.isdigit() and is_0_255(x), ip.split('.')))
result = all(result_list)
print(result)

