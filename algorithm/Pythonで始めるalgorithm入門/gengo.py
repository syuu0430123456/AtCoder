#元号に変換

def convert_gengo(year):
    seireki = year
    if not 1868<=year<=2020:
        print("1869から2020で入力してください")
    else:
        if 1868<=year<1912:
            is_gengo = '明治'
            year -= 1867
        elif 1912<=year<1926:
            is_gengo = '大正'
            year -= 1911
        elif 1926<=year<1989:
            is_gengo = '昭和'
            year -= 1925
        elif 1989<=year<2019:
            is_gengo = '平成'
            year -= 1988
        else:
            is_gengo = '令和'
            year -= 2018
    
    if year == 1:
        year = '元年'
    else:
        year = str(year) + '年'

    return is_gengo + year

for i in range(1869,2020):
    print(str(convert_gengo(i)))