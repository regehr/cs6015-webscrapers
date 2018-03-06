from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys, datetime
from bs4 import BeautifulSoup
usernameInput = sys.argv[1]
passwordInput = sys.argv[2]

driver = webdriver.Chrome('/Users/madelineluke/Downloads/chromedriver')
currentdate = datetime.datetime.now().strftime("%Y-%m-%d")
driver.get('https://utah.instructure.com/calendar#view_name=month&view_start=' + currentdate)

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys(usernameInput)
password.send_keys(passwordInput)

driver.find_element_by_name("submit").submit()
sleep(10)

currentdate = datetime.datetime.now().strftime("%Y-%m-%d")

first = driver.find_element_by_class_name('ic-app')
page = first.find_element_by_id('calendar-app')
container = page.find_element_by_class_name('fc-view-container')
tbody = container.find_element_by_class_name('fc-body')
td = tbody.find_element_by_class_name('fc-widget-content')
div = td.find_element_by_class_name('fc-day-grid-container')
div1 = div.find_element_by_class_name('fc-day-grid')

weeks = div1.find_elements_by_class_name('fc-content-skeleton')
for w in weeks:
    events = w.find_elements_by_class_name('fc-event-container')
    # dates = w.find_elements_by_class_name('fc-day-number')
    for e in events:
        date = w.find_element_by_class_name('fc-day-number')
        actualDate = date.get_attribute('data-date')
        if actualDate >= currentdate:
            print date.get_attribute('data-date')
        # print "found events"
            eventNames = e.find_elements_by_class_name('fc-day-grid-event')
            for names in eventNames:
                print names.get_attribute('title')
