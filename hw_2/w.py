f = open('weather.log', 'r', encoding='utf-8')
t = f.readlines()
f.close()

while True:
    temp_log = []
    air = 0
    humidity = 0
    sea = 0
    total_days = 0
    max_air = [None, None]
    min_air = [None, None]
    max_sea = [None, None]
    min_sea = [None, None]


    for n, v in enumerate(t):
        temp_log.append(v.split())
        temp_log[n][0] = temp_log[n][0].split('-')
        temp_log[n][0][1] = int(temp_log[n][0][1])


    month = int(input('Type month to analyze temperature (only: 1, 2, 9, 10, 11, 12): '))

    for v in temp_log:
        if v[0][1] != month:
            pass
        else:

            val_air = float(v[2].replace('°C,', ''))
            val_sea = float(v[4][1:].replace('°C', ''))
            if total_days == 0:
                max_air = [val_air, v[0][2]]
                min_air = [val_air, v[0][2]]
                max_sea = [val_sea, v[0][2]]
                min_sea = [val_sea, v[0][2]]
            else:
                if val_air > max_air[0]:
                    max_air[0], max_air[1] = val_air, v[0][2]
                elif val_air < min_air[0]:
                    min_air[0], min_air[1] = val_air, v[0][2]
                if val_sea > max_sea[0]:
                    max_sea[0], max_sea[1] = val_sea, v[0][2]
                elif val_sea < min_sea[0]:
                    min_sea[0], min_sea[1] = val_sea, v[0][2]


            air += val_air
            sea += val_sea
            humidity += int(v[3].replace('%,', ''))
            total_days += 1

    print(f"Average: \n* °t air: {round(air/total_days, 1)} °C, \n* °t sea: "
          f"{round(sea/total_days, 1)} °C, \n* humidity: {round(humidity/total_days, 0)} %")
    print(f"Maximus/Minimus:\n* max °t air:\t{max_air[0]}°C / ({max_air[1]}.{month})"
          f"\n* min °t air:\t{min_air[0]}°C / ({min_air[1]}.{month})"
          f"\n* max °t sea:\t{max_sea[0]}°C / ({max_sea[1]}.{month})"
          f"\n* min °t sea:\t{min_sea[0]}°C / ({min_sea[1]}.{month})")
    print(f"total records: {total_days}")

