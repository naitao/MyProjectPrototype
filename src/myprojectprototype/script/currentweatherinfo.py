import time
from myprojectprototype.script import weatherinfo

def main():
    currentWeather_url = 'http://api.openweathermap.org/data/2.5/weather?id=2964574&appid=3641377121f997a81e12f28ba9831df1'
    filename = 'currentWeather.csv'
    my = weatherinfo.Weatherinfo(currentWeather_url)
    while True:
        ret1 = my.to_csv2(filename)
        ret2 = my.import_to_mysql(csv_file=filename)
        if ret1 == 0 and ret2 == 0:
            print("Current weather information is updated into RDS (30mins)")
        else:
            print("Current weather information is failed to update into RDS")
        # update current information ont RDS every 30 mins
        time.sleep(1800)


if __name__ == '__main__':
    main()
