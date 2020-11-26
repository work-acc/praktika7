# Варинт 18. В списке, состоящем из вещественных элементов, вычислить:
# 1) произведение отрицательных элементов списка;
# 2) сумму положительных элементов списка, расположенных до максимального элемента.
# Изменить порядок следования элементов в списке на обратный.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    # Ввести список одной строкой.
    a = tuple(map(int, input().split()))
    # Если список пуст, завершить программу.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)
    # Найти искомую сумму.
    s = 1
    for item in a:
        if item < 0:
            s *= item
    print(s)
