# -*- coding:utf-8 -*-

count = 0


def change(target, coins, usable):
    global count
    coin = coins.pop(0)
    if len(coins) == 0:
        if target / coin <= usable:
            count += 1
    else:
        target_coin = (target / coin) + 1
        for i in range(0, target_coin):
            change(target - coin * i, coins[:], usable - i)


def main():
    bill = 1000
    global count
    change(bill, [500, 100, 50, 10], 15)
    print(count)


if __name__ == '__main__':
    main()
