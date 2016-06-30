# -*- coding:utf-8 -*-


# 2進数、8進数、10進数の回文数を求める処理
def main():
    # 11から探索開始
    x = 11

    while True:
        if str(x) == str(x)[::-1] \
                and str(format(x, 'b')) == str(format(x, 'b'))[::-1] \
                and str(format(x, 'o')) == str(format(x, 'o'))[::-1]:
            print(x)
            break
        x = x + 2


if __name__ == '__main__':
    main()
