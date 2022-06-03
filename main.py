import pandas as pd
import time
import re
import time
from datetime import datetime, timedelta

def main():
    csv_file = pd.read_csv('TwitterPoldaMetroJaya.csv')
    data = csv_file[["X.1", "X.2"]]
    data_l = data.values.tolist();

    URL_PATTERN = r'[A-Za-z0-9]+://[A-Za-z0-9%-_]+(/[A-Za-z0-9%-_])*(#|\\?)[A-Za-z0-9%-_&=]*'
    regx = re.compile(URL_PATTERN);

    i = 1
    for col in data_l:
        print(i, end='. ')
        print(col[1])
        i += 1

    print('='*100)

    # remove any link
    for data in data_l:
        if regx.search(data[0]):
            data[0] = re.sub(URL_PATTERN, '', data[0])

    # remove empty list
    n = 0
    for data in data_l:
        if not data[0]:
            data_l.pop(n)
        n += 1

    # convert twitter timestamp to gmt +7
    for data in data_l:
        data[1] = to_gmt7(data[1])

    # get data that contain trafic information
    # remove hour

    i = 1
    for col in data_l:
        print(i, end='. ')
        print(col)
        i += 1


def to_gmt7(twitter_date):
    date = datetime.strptime(twitter_date, "%Y-%m-%d %H:%M:%S")
    to_timestamp = date.timestamp()
    d_add = to_timestamp + 25200 #7 Hours
    to_date = datetime.fromtimestamp(d_add)

    return to_date.strftime("%d %B %Y %H:%M:%S")

if __name__ == '__main__':
    main()
    # format_date = datetime.strptime(twitter_date, "%m/%d/%Y %I:%M:%S %p")
    # timestamp = format_date.timestamp()
    #
    # print(timestamp)
    # print(timestamp + 25200)
    # print('=======================')
    # print(format_date)
    # print(datetime.fromtimestamp(timestamp + 25200))
    # twdate_split = ' '.join(twitter_date.split(" ")).split()
    #
    # date = twdate_split[0]
    # time = twdate_split[1]
    # time_system = twdate_split[2]
    #
    # t_add = int(time.split(':')[0]) + 7
    # time = time.replace(time.split(':')[0], str(t_add))
    #
    # if time_system == 'PM' and int(time.split(':')[0]) > 11 :
    #     t_cday = time.split(':')[0]
    #     print(t_cday)

    # print(time)