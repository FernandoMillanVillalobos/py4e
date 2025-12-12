name = input("Enter file:")
try:
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
except:
    print("File cannot be opened:", name)
    exit()

counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for k, v in counts.items():
    newtup = (k, v)
    lst.append(newtup)
lst = sorted(lst)
for k, v in lst:
    print(k, v)