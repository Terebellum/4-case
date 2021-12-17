# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

    # Ввод
    s = []
    r = 1
    for i in range(0, 3):
        a = int(input())
        r *= a
        s.append(a)
    
    #Вывод значения
    print(r)
