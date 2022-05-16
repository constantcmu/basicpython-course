from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


def writetocsv(data):

    date = datetime.now().strftime('%Y-%m-%d')
    with open('data-temperature-{}.csv'.format(date),'a',newline ='',encoding='utf-8') as file:
        filewriter = csv.writer(file)
        filewriter.writerow(data)

alldata = {}
def checktemp(ID):
    url = 'https://www.tmd.go.th/province.php?id='+str(ID)
    webopen = urlopen(url)
    html_page = webopen.read()
    webopen.close()

    data = BeautifulSoup(html_page,'html.parser')
    try:
        temp = data.find('td',{'class':'strokeme'})
        title = data.find('span',{'class':'title'})
        city = title.text.strip()
        temp = temp.text
    
        alldata[city] = temp
    except:
        pass


for i in range(1,100):
    checktemp(i)


for k,v in alldata.items():
    data = [k,v]
    writetocsv(data)
    
print('saved')