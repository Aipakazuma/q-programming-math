# -*- coding:utf-8 -*-


def main():
    # 1~100までのカードがあって、2番目から1枚おきにカードを裏返す（2...4...6...）
    # 次に3番目から2枚おきにカードを裏返す。この時裏返ってきたカードは表を向く(3...6...9)
    # n番目のカードから、n-1枚おきにカードを裏返す操作をどのカードの向きも変わらなくなるまで続ける
    # この時、裏向きになっているカードの番号をすべて求めてください

    # 表をTrue,裏をFalseなlistを作る
    cards = [False for i in range(1, 101)]

    # ややこしいけど、要素数は0からスタートなのでこんな => range(1, 100) => 2 ~ 99
    for n in range(2, 101):
        # n - 1
        nn = n - 1
        while nn < len(cards):
            # bool反転
            cards[nn] = not cards[nn]
            nn += n

    for index, card in enumerate(cards):
        # 裏向きにになっている、index番号+1を取得
        if card is False:
            print(index + 1)


if __name__ == '__main__':
    main()
