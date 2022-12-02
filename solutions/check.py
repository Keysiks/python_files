menu = {}
for _ in range(int(input())):
    ice_cream, price = input().rsplit(maxsplit=1)
    menu[ice_cream] = int(price)

input()

order_sums = [0]
for order in iter(input, "."):
    if order:
        ice_cream, count = order.rsplit(maxsplit=1)
        order_sums[-1] += menu[ice_cream] * int(count)
    elif order_sums[-1] != 0:
        order_sums.append(0)

total_sum = 0
for i, order_sum in enumerate(order_sums):
    total_sum += order_sum
    if order_sum != 0:
        print(f"{i + 1}) {order_sum}")
print("Итого:", total_sum)
