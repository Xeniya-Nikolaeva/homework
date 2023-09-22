from random import randint
b = 5000000 #размер списка
a = []
for i in range(b):
        a.append(randint(1, 999999))

for i in range(b-1):
        for j in range(b-i-1):
                if a[j] > a[j+1]:
                        a[j], a[j+1] = a[j+1], a[j]

for i in range(len(a)): #выводим список в столбик
        print(a[i])

