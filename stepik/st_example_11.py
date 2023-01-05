

count = 0

def is_score(line):
    scores = map(int, line.strip().split()[1:])
    res = all(map(lambda x: x >= 65, scores))
    return res

with open('grades.txt', 'r', encoding='utf-8') as file:
    for line in file:
        if is_score(line):
            count += 1
print(count)