#うるう年
#4で割り切れる年
#100で割り切れて400で割り切れる年

def is_leap_year(year):
    if year%4==0:
        if year%100==0 and year%400 != 0:
            return False
        else:
            return True
    else:
        return False

for i in range(100,2101,100):
    print(str(i)+ ' ' +str(is_leap_year(i)))