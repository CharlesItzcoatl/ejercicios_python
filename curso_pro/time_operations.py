from datetime import datetime, timedelta

def time_sum():
    my_list = []
    num = int(input('Cantidad de elementos: '))
    for i in range(num):
        my_list.append(datetime.strptime(input('Tiempo {i}: '.format(i=i+1)), '%M:%S'))
    # time_List = my_list
    # my_sum = timedelta()
    # for i in time_List:
    #     (m, s) = i.split(':')
    #     d = timedelta(minutes=int(m), seconds=int(s))
    #     my_sum += d
    # print(my_sum)
    time_sum = datetime(year=1900, month=1, day=1, hour=0, minute=0, second=0)
    for song in my_list:
        time_sum += timedelta(minutes=song.minute)
        time_sum += timedelta(seconds=song.second)

    print(str(time_sum.hour) + ':' + str(time_sum.minute) + ':' + str(time_sum.second))


if __name__ == '__main__':
    time_sum()