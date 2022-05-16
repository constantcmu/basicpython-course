import csv
from datetime import datetime


def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    with open('data-temperature-{}.csv.format(date)','a',newline ='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)


writetocsv(['กทม',20.5])
