# -*- coding:utf-8 -*-


# 2進数、8進数、10進数の回文数を求める処理
def main():
    # 11から探索開始
    x = 11

    while True:
        # 型もチェックするので、合わせる
        # format()はint型でないとエラーになる
        # format(b)はbinary(2進数)、format(o)はoctal(8進数)
        # str()にしたあとに[::-1]をすると文字列が逆に並ぶ（すごい）
        if str(x) == str(x)[::-1] \
                and str(format(x, 'b')) == str(format(x, 'b'))[::-1] \
                and str(format(x, 'o')) == str(format(x, 'o'))[::-1]:
            print(x)
            break

        # python3からこの表記はおｋになった？
        x += 2


if __name__ == '__main__':
    main()
