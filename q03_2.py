# -*- coding:utf-8 -*-


def main():
    # 1~100まで1度評価した箇所は反転しないということなので
    # 1~100ループ => 1~100のループ => n % oで余りが無しの条件でカードを反転する
    # 1~100反転loop => 奇数回 => True
    # 2~100反転loop => 偶数回 => False
    # 3~100反転loop => 偶数回 => False
    # 4~100反転loop => 奇数回 => True
    # 10~100反転loop => 偶数回 => False
    # 16~100反転loop => 奇数回 => True
    for n in range(1, 101):
        flag = False
        for o in range(1, 101):
            if n % o == 0:
                flag = not flag
        if flag is True:
            print(n)

if __name__ == '__main__':
    main()
