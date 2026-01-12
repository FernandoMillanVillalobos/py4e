import re

hand = open("regex_sum_42.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    x = re.findall("[0-9]+", line)
    if len(x) > 0:
        for i in x:
            numlist.append(int(i))
print(sum(numlist))
