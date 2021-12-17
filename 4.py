# !/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":

    # Список
    s = list(map(float, input().split()))

    # Нахождение суммы нечетных
    sum1 = sum(s[i] for i in range(0, len(s)) if i % 2 != 0)
    print(sum1)
    
    # Нахождение суммы между первым и последним отрицательным
    sum2 = sum(s[min([i for i in range(0, len(s)) if s[i] < 0])+1:max([i for i in range(0, len(s)) if s[i] < 0]):])
    print(sum2)
    
    #Сжатие списка
    s.reverse()
    End = True
    for i in range(0, len(s)):
        if i < len(s):
            if abs(s[i]) < 1:
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
