import sys
import datetime





def isInInterval(duration, mytime):
        return int(duration[0]) <= mytime/1000 <= int(duration[1])

def getClock(interval, timestamp):
    for key,value in interval.items():
        reminder = int(timestamp/1000 % (3600*24)) * 1000
        if isInInterval(value, reminder):
            return key    

def getDate(timestamp):
    dateStr = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return dateStr

def main():
    '''
    plots = list(range(24))

    interval = {}
    for i in plots:
        interval[i+1] = ([i*3600, (i+1)*3600-1])
    print(interval)
    print(getClock(interval, 1522916716000))
    '''
    if len(sys.argv) == 2:
        print(getDate(float(sys.argv[1])))

if __name__ == '__main__':
    main()
