#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
import datetime 

path = 'C:/Users/nt16145/Documents/JR_mars/chromedriver_win32/chromedriver.exe'
#指定するブラウザを開く
driver = webdriver.Chrome(executable_path=path)
#指定URLのページを開く
driver.get('http://r113.sakura.ne.jp/p/ticket-sim/mars/index.html')
path = 'C:/Users/nt16145/Documents/JR_mars/mars156.txt'
file = open(path)
text = file.readlines()

# print(text[1])

text_split = text[1].split()

# print(text_split[0])
Select(driver.find_element_by_name('typeSelect')).select_by_value('type-joshaken')
if '新幹線' in text[3]:
    Select(driver.find_element_by_name('shinkansenMarkSelect')).select_by_value('shinkansen-mark')
else:
    Select(driver.find_element_by_name('shinkansenMarkSelect')).select_by_value('null')
Select(driver.find_element_by_name('adultChildSelect')).select_by_value('null')
Select(driver.find_element_by_name('holePositionSelect')).select_by_value('non')
driver.find_element_by_id('kanzaiRouteExistCheckbox').click()
# date = driver.find_element_by_id('yukoKigenDateInput1').text
date = datetime.date.today().day
pattern = r'([0-9])'
expiration =  re.findall(pattern,text[11])
print(text)
print(expiration)
date = int(date) + int(expiration[0]) - 1
month = datetime.date.today().month
if month is 1 or 3 or 5 or 7 or 8 or 10 or 12:
    if date > 31:
        month = int(month) + 1
        date = int(date) - 31
elif month is 4 or 6 or 9 or 11:
    if date > 30:
        month = int(month) + 1
        date = int(date) - 30
else:
    if date > 28:
        month = int(month) + 1
        date = int(date) - 28
if month is 13:
    month = int(month) - 12
driver.find_element_by_id('yukoKigenDateInput2').clear()    
driver.find_element_by_id('yukoKigenDateInput3').clear()
driver.find_element_by_id('yukoKigenDateInput2').send_keys(month)
driver.find_element_by_id('yukoKigenDateInput3').send_keys(date)
driver.find_element_by_id('fareInput').clear()
pattern = r'\D'
fee_split = text[8].split()
fee =  re.sub(pattern,'',fee_split[2])
# print(fee)
driver.find_element_by_id('fareInput').send_keys(fee)
driver.find_element_by_id('stationInput0').clear()
driver.find_element_by_id('stationInput0').send_keys(text_split[0])
driver.find_element_by_id('stationInput1').clear()
driver.find_element_by_id('stationInput1').send_keys(text_split[2])
pattern = r'[+-]?[0-9]+[\.]?[0-9]*[eE]?[+-]?[0-9]*'
distance_split = text[5].split()
distance = re.findall(pattern,distance_split[1])
if float(100) < float(distance[0]):
    Select(driver.find_element_by_name('discountSelect')).select_by_value('discount/student')
else:
    Select(driver.find_element_by_name('discountSelect')).select_by_value('null')
Select(driver.find_element_by_name('printStationSelect')).select_by_value('sapporo-nishi-mv3')
Select(driver.find_element_by_name('printCompanySelect')).select_by_value('1')
driver.find_element_by_id('rightPurpleNumCheckbox').click()
