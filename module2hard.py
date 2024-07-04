import random

str1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
str2 = []


def stolb(n):
    parol = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                parol += str(i) + str(j)
    return parol


n = random.choice(str1)
parol = stolb(n)
print(n, parol)