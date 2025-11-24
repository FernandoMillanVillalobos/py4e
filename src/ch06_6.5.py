# fruit = "banana"
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(index, letter)
#     index = index + 1

# for letter in fruit:
#     print(letter)

# count = 0
# for letter in fruit:
#     if letter == 'a':
#         count = count + 1
# print("Number of a's:", count)

# if "n" in fruit:
#     print("Found it!")

# stuff = "Hello\nWorld"
# x = type(stuff)
# y = dir(stuff)
# print(x, y)

# x = fruit.find("na")
# print(x)

# y = fruit.find("z")
# print(y)

# greet = "Hello Bob"
# y = greet.replace("Bob", "Jane")
# print(y)˙˙
# x = greet.replace("o", "x")
# print(x)

# greet = "   Hello Bob   "
# print(greet.lstrip())
# print(greet.rstrip())
# print(greet.strip())

# line = "Please have a nice day"
# print(line.startswith("Please"))
# print(line.startswith("p"))

# data = "From stephen.marquart@uct.ac.za Sat Jan  5 09:14:16 2008"
# atpos = data.find("@")
# sppos = data.find(" ", atpos)
# host = data[atpos+1 : sppos]
# print(host)

text = "X-DSPAM-Confidence:    0.8475"
i = text.find("0")
fnum = float(text[i:])
print(fnum)