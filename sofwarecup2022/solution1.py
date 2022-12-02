n = int(input())
a0, a1, a2, a3, a4 = (int(input()) for i in range(5))
price = {'a0': a0, 'a1': a1, 'a2': a2, 'a3': a3, 'a4': a4}
# проверить для n  = степени двойки

count_list = {'a0': n // 16 + 1 if n % 16 != 0 else n // 16, 'a1': n // 8 + 1 if n % 8 != 0 else n // 8,
              'a2': n // 4 + 1 if n % 4 != 0 else n // 4, 'a3': n // 2 + 1 if n % 2 != 0 else n // 2, 'a4': n}

lst = [price[el] * count_list[el] for el in price.keys()]
print(min(lst))
