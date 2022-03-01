#여기에서 원격으로 사이트를 조종하는 것
#chromedriver 다운로드: https://chromedriver.chromium.org/downloads
#크롬버전 확인: chrome://version/

from selenium import webdriver
#브라우저 열기
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('http://naver.com')

#이동
browser.find_element_by_class_name('link_login').click()  #class내용을 입력함. 로그인 페이지로 이동
browser.back()
browser.forward()
browser.refresh()          


#검색창에 해당 워드를 입력
from selenium.webdriver.common.keys import Keys

query = browser.find_element_by_id('query')  #검색창은 id를 확인 혹은 name
query.send_keys('멀티캠퍼스')
#엔터까지 실행.
query.send_keys(Keys.ENTER)


#태그 받아오기 앞에서했던 requests soup과정
#a태그 받아오기
tag = browser.find_element_by_tag_name('a')
print(tag)

#모든 a태그 받아오기
tags = browser.find_elements_by_tag_name('a')

for tag in tags:
    print(tag.get_attribute('href'))



#daum.net 으로 이동
browser.get('https://www.daum.net/')

query = browser.find_element_by_name('q')
query.send_keys('멀티캠퍼스')
query.send_keys(Keys.ENTER)

browser.find_element_by_xpath('').click()
browser.quit()












