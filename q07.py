# -*- coding:utf8 -*-

from datetime import datetime, date, timedelta

def date_format_yyyymmdd(date):
    return date.strftime('%Y%m%d')


def to_binary_number(i, radix_string='b'):
    return format(i, radix_string)


def to_decimal_number(i, radix=2):
    return int(i, radix)


def main():
    '''
    年月日をYYYYMMDDの８桁の整数で表したとき、これを２進数に変換して逆から並べ
    さらに10進数に戻した時、元の日付と同じ日付になるものを探してください。
    期間は1964/10/10から、2020/7/24とします。

    example)
    case 1966/7/13
    1. YYYYMMDD -> 19660713
    2. 2進数 ->   1001010111111111110101001
    3. revers -> 1001010111111111110101001
    3. to 10 -> 19660713
    :return:
    '''

    start_date = date(1964, 10, 10)
    end_date = date(2020, 7, 24)
    diff_date = (end_date - start_date).days
    for day in (start_date + timedelta(x) for x in range(diff_date)):
        date_format = int(date_format_yyyymmdd(day))
        binary_number = to_binary_number(date_format)
        binary_number_reverse = binary_number[::-1]
        after_reverse = to_decimal_number(binary_number_reverse, 2)
        if date_format == after_reverse:
            print(binary_number)
            print(day)

def main_ver2():
    '''
    取得したい値には規則性がある
    左4桁が 1001
    右4桁が 1001
    である

    というか25桁の真ん中をとった24桁は対象であります。
    真ん中はの数字は0か1なので、それでループします。

    :return:
    '''
    start_date = date(1964, 10, 10)
    end_date = date(2020, 7, 24)
    from_left = int(format(int(start_date.strftime('%Y%m%d')), 'b')[4:12], 2)
    to_left = int(format(int(end_date.strftime('%Y%m%d')), 'b')[4:12], 2)
    for i in range(from_left, to_left):
        l = format(i, 'b')
        r = l[::-1]
        for j in range(2):
            value = '1001' + str(l) + str(j) + str(r) + '1001'
            try:
                print(datetime.strptime(str(to_decimal_number(value, 2)), '%Y%m%d').date())
            except:
                pass

if __name__ == '__main__':
    main_ver2()
