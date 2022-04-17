def season(month):
    if month == 12 or month >= 1 and month <= 2:
        return 'WINTER'
    elif month >= 3 and month <= 5:
        return "SPRING"
    elif month >= 6 and month <= 8:
        return "SUMMER"
    elif month >= 9 and month <= 11:
        return "AUTUMN"
    else:
        return "Wrong month number!!!"


while 1:
    number = int(input("Input month number and I'll tell you the season: "))
    print(season(number))
