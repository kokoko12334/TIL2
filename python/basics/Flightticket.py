from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import configparser
import datetime
import calendar

class FlightTicket():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('./confi.ini')
        self.browser = webdriver.Chrome('./chromedriver.exe')

    def getweekno(self, month, day):
        year = datetime.datetime.now().date().year
        
        firstWeekday = calendar.weekday(year, month, 1) 
        firstSunday = 7-firstWeekday
        weekno = (day-firstSunday)//7 +2

        return weekno, calendar.weekday(year, month, day)


    def setDay(self, way):
        if way == 'DEPARTURE':
            WebDriverWait(self.browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,
            '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]'))).click()
            month = int(self.config['DEPARTURE']['MONTH'])
            day = int(self.config['DEPARTURE']['DAY'])
            self.getweekno(month, day)
            
            weekno, weekday = self.getweekno(month, day)
            self.browser.find_element(By.XPATH, 
            f'//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[{month}]/table/tbody/tr[{weekno}]/td[{(weekday+2)%7}]/button/b')
            
    def reserve(self):
        self.browser.maximize_window()

        url = 'https://flight.naver.com/'
        self.browser.get(url)
      





if __name__ == '__main__':
    ticket = FlightTicket()
    ticket.reserve()



















