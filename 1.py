# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

    # Ввод
    s = []
    for i in range(0, 10):
        a = int(input())
        s.append(a)

    # Нахождение позиции наибольшего
    a = s[0]
    for i in range(1, 10):
        if (s[i] > a):
            pos = i
            a = s[i]
    
    #Замена двух частей списка
    first = s.pop(0)
    second = s.pop(pos-1)
    s.insert(pos, first)
    s.insert(0, second)

    #Вывод списка
    for i in range(0, 10):
        print(s[i])
