#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import math

if __name__ == '__main__':
    # Ввести кортеж одной строкой.
    a = tuple(map(int, input().split()))
    # Если кортеж пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    #  2) сумму положительных элементов кортежа,
    #       расположенных до максимального элемента.
    # Вторая часть
    b = max(a)
    f = -1
    e = 0
    for i in a:
        f += 1
        if i == b:
            e = f

    s = 0
    for k in range(e):
        s += a[k]
    print("Сумма: ", int(s))

    a = tuple(reversed(a))
    print(a)