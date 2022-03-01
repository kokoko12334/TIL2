import csv
import re
from bs4 import BeautifulSoup
import requests



url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
filename = '시총top200.csv'

with open('./output/'+filename, 'w', encoding = 'utf-8-sig', newline = '') as f:
    writer = csv.writer(f)
    title = 'N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실'.split('\t')
    # title = ''.join(title).replace('\t', ',').split(',')
    writer.writerow(title)

    for page in range(1,5):   #각 페이지
        res = requests.get(url + str(page))
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        data_rows = soup.find('table', attrs = {'class':'type_2'}).find('tbody').find_all('tr')

        for row in data_rows:  #행 하나당
            columns = row.find_all('td')
            if len(columns) <= 1:
                continue
            data = [column.get_text().strip() for column in columns] #행 하나의 각 열
                  
            writer.writerow(data)






