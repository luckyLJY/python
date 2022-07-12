import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = './data/sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[2],"%Y-%m-%d")
            high = int(row[8])
            low = int(row[9])

        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # 根据数据绘制图形

    fig = plt.figure(dpi = 128,figsize=(10,6))
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)

    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    # 设置图形的格式
    # 这是字体大小和标签
    plt.title("Daily high and low temperatures-2014", fontsize=24)
    plt.xlabel('Date', fontsize=16)


    # 为了避免X轴日期显示彼此重叠，调用该方法，将以倾斜的形式显示日期标签
    fig.autofmt_xdate()

    # 设置标签
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

