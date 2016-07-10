# -*- coding:utf-8 -*-


def main(m, n):
    count = 0
    current = 1
    # 棒の最大cm1と現在の棒の数をカウント
    while n > current:
        # 棒の数が人数より小さければ現在の棒の数を返す
        current += current if current < m else m
        # 結合した数をカウントする
        count += 1

    return count

if __name__ == '__main__':
    print(main(3, 20))
    print(main(5, 100))
