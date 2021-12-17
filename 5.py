# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

    # Список
    s = list(map(float, input().split()))

    # Максимальное число
    m = max(s)
    print(m)

    # Сумма до последнего положительного
    sum1 = sum(s[:(max(i for i in range(0, len(s)) if s[i] > 0))+1])
    print(sum1)


    #Сжатие списка
    a = float(input())
    b = float(input())
    s.reverse()
    End = True
    for i in range(0, len(s)):
        if i < len(s):
            if a <= abs(s[i]) <= b:
                if End == True:
                    s[i] = 0
                else:
                    del s[i]
                    i -= 1
            else:
                End = False
        else:
            break
    s.reverse()

    #Вывод списка
    for i in range(0, len(s)):
        print(s[i])
