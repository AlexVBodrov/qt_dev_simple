# put your python code here
classes = int(input())
count = 0
for klass in range(classes):
    count_s = range(int(input()))
    for s in count_s:
        name, score = input().split()
        if score == '5':
            count += 1
if classes == count:
    print('YES')
else:
    print('NO')