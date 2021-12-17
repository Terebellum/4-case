# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

    # Ввод
    s = []
    for i in range(0, 10):
        a = int(input())
        s.append(a)

    # Нахождение позиции наибольшего и наименьшего
    a = s[0]
    b = s[0]
    for i in range(1, 10):
        if (s[i] > a):
            posmax = i
            a = s[i]
        elif (s[i] < b):
            posmin = i
            b = s[i]
    
    #Замена двух частей списка
    if posmax > posmin:
        minimal = s.pop(posmin)
        maximal = s.pop(posmax-1)
    else:
        maximal = s.pop(posmax)
        minimal = s.pop(posmin - 1)
    s.insert(posmin, maximal)
    s.insert(posmax, minimal)

    #Вывод списка
    for i in range(0, 10):
        print(s[i])
