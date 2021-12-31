import re


class Pair:
    def __init__(self, word, times):
        self.word = word
        self.times = times

    def __repr__(self):
        return "Pair - Number: % s - Times: % s" % (self.word, self.times)


x = "I am 15 years old, my roommate is 17, and my friend is 14"
y = re.findall("[0-9]", x)
print("Numbers as a single or separated: ", y)

x1 = "I am 15 years old, my roommate is 17, and my friend is 14"
y1 = re.findall("[0-9]+", x1)
print("Numbers together or exactly as they are in the text:", y1)

a = "Hello my name is Mateo and I like Python."
b = re.findall("[aeiou]", a)  # Code for finding letters. + func is the same
print(b)

decision = int(input("Enter 1. for numbers separated, or enter 2. for numbers "
               "together: "))

if decision == 1:
    x2 = "7bb47b4277abb9d2bb0d954204d30e5467d98425ee994054974242ccfd16a191"
    y2 = re.findall("[0-9]", x2)
    res2 = []
    for i in y2:
        if i not in res2:
            res2.append(i)
    print("Numbers separated or individually: ", res2)
    for num in res2:
        pair = Pair(num, y2.count(num))
        print(pair)
elif decision == 2:
    x3 = "7bb47b4277abb9d2bb0d954204d30e5467d98425ee994054974242ccfd16a191"
    y3 = re.findall("[0-9]+", x3)
    res3 = []
    for num in y3:
        if num not in res3:
            res3.append(num)
    print("Numbers together: ", res3)
    for num in res3:
        pair = Pair(num, y3.count(num))
        print(pair)
