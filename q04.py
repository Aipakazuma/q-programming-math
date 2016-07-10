# -*- coding:utf-8 -*-


def cut_bar(m, n, current):
    if n <= current:
        # 切り終えた
        return 0
    elif current < m:
        # 次は現在の２倍
        return 1 + cut_bar(m, n, current * 2)
    else:
        # はさみの数だけ追加
        return 1 + cut_bar(m, n, current + m)


def main():
    # 長さ n cmの棒
    # １本の棒は1人でしか切れない
    # 棒は最後には1cm単位にする
    # 最大 m 人の人がいるとき、最短何回できれる？
    n = 20
    m = 3

    print(cut_bar(3, 20, 1))
    print(cut_bar(5, 100, 1))

if __name__ == '__main__':
    main()
