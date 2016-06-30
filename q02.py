# -*- coding:utf-8 -*-


def main():
    # 1000~9999までで、四則演算したあとに逆順になる値を探せ

    # *と空文字だけでも良い
    op = ['+', '-', '*', '/', '']
    for num in range(1000, 10000):
        for i in range(0, len(op)):
            for j in range(0, len(op)):
                for k in range(0, len(op)):
                    # charではなくstringにして配列指定で１文字が取れる
                    first = str(num)[0]
                    second = str(num)[1]
                    third = str(num)[2]
                    four = str(num)[3]

                    opi = op[i]
                    opj = op[j]
                    opk = op[k]

                    # 0~みたいな数値は存在せず、Pythonではエラーになるので可能性のある文字は除外する
                    # どうせ0が混じった計算は結果0になるので、比較できない（はず）
                    if second == '0'\
                        or third == '0' \
                        or four == '0':
                        continue

                    formula = first + opi + second + opj + third + opk + four
                    # 四則演算１文字は必ずいれて計算する
                    if 4 < len(formula):
                        # evalで文字列をコードとして実行
                        result = eval(formula)

                        # 結果の逆数値と元数値が一緒であるか確認
                        if int(str(num)[::-1]) == result:
                            print(formula)
                            print(num)
                            break

if __name__ == '__main__':
    main()
