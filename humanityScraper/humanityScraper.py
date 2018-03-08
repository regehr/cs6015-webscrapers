import re, sys
import getpass

from bs4 import BeautifulSoup
from selenium import webdriver
import time

'''
humanityScraper.py
written by Irene Yeung

This is a simple web scraper written in Python 3 that accesses a specific
work scheduling website (i.e., https://www.humanity.com) and retrieves the employee work schedule
based on specified commandline arguments.
It automates the site login process, using Selenium WebDriver for Google Chrome,
then parses html of the site pages for schedule data.
'''

def validate_input(argv1, argv2):
    validparams = [('mine', 'daily'), ('mine', 'weekly'), ('all', 'daily'), ('all','weekly'), ('all', 'monthly')]
    if (argv1, argv2) not in validparams:
        print('Invalid schedule criteria.')
        return False
    return True

def init_driver(): #initializes Selenium WebDriver in google Chrome
    driver = webdriver.Chrome()
    driver.implicitly_wait(3) #wait for website to load
    return driver

def user_login(url):
    print("Please enter your Humanity login credentials:\n")
    user_name = getpass.getpass(prompt='Email/Username: ', stream=None)
    if len(user_name) == 0:
        user_name = 'yeung.ireneh@utah.edu' #default email
    my_pwd = getpass.getpass(prompt='Password: ',stream=None) #hides password input
    login = url+'/app/'
    print("\n\tLogging in, please wait . . .")
    driver = init_driver()
    driver.get(login)
    time.sleep(2)
    driver.find_element_by_id('email').click()
    time.sleep(1)
    driver.find_element_by_id('email').send_keys(user_name)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').send_keys(my_pwd)
    time.sleep(1)
    driver.find_element_by_name('login').click() #submit form with login info
    return driver

def get_work_schedule(argv1, argv2, url, driver):
    assert argv1 == 'mine' or argv1 == 'all' #probably redundant because of validate input method
    print('\n\tLogin Successful. Please wait while schedule data is generated. . .\n')
    if argv1 == 'mine':
        print_my_upcoming_shifts(argv2, driver)
        return
    time.sleep(3)
    driver.get(url + '/app/schedule/') #navigate from dashboard to schedule view
    time.sleep(2)
    #switch from my schedule to schedule overview by clicking radio button
    driver.find_element_by_id('cb_overview').click()
    time.sleep(2)
    #default schedule view is weekly
    if argv2 == 'daily':
        driver.find_element_by_id('tls_day').click()
    elif argv2 == 'monthly':
        driver.find_element_by_id('tls_month').click()
    time.sleep(2)
    #change from default employee view to list view for easier parsing
    driver.find_element_by_id('tlv_list').click()
    time.sleep(2)
    print_upcoming_schedule(argv2, driver)
    return

def print_upcoming_schedule(argv2, driver):
    htmlsrc = driver.page_source
    soupall = BeautifulSoup(htmlsrc, 'html.parser')
    #extract date range to precede schedule data output
    daterange = soupall.find(id="_ddrl").get_text()
    #print title for schedule overview
    print('\tEmployee Schedule Overview\n\tDate Range:' + daterange + '\n')
    #iterate over tr's within table containing shift data
    for r in soupall.find("table", id="shiftlist").find_all("tr"):
        #if td tag with class = demp is found, found date header for each entry
        if r.find("td", class_="demp"):
            print('\n' + r.find("td", class_="demp").get_text() + '\n')
        else: #rest of tr entries in shfitlist table are employee shifts
            time = r.find("td", class_="second").get_text()
            strjobtitles = re.search(r'\d.+', time).group(0) #strips job title preceding shift time
            employee = r.find("td", class_="third").get_text()
            print(strjobtitles + ' ' + employee)
    return

def print_my_upcoming_shifts(argv2, driver):
    time.sleep(5) #wait for page to load before printing any text to terminal
    print(time.strftime("Today's Date: %A, %B %d, %Y"))
    print()
    text = 'Upcoming Shifts:'
    if argv2 == 'daily':
        text = 'Next Upcoming Shift:'
    print(text)
    htmlsrc = driver.page_source
    soupme = BeautifulSoup(htmlsrc, 'html.parser')
    shiftsdiv = soupme.find(class_='upcomingShift__body')
    if not shiftsdiv:
        print('You have no upcoming shifts.')
        return
    elif shiftsdiv:
        shiftmonths = shiftsdiv.find_all(class_='upcomingShift__mname')
        shiftdates = shiftsdiv.find_all(class_='upcomingShift__day')
        shifttimes = shiftsdiv.find_all(class_='upcomingShift__time')
        assert len(shiftmonths) == len(shiftdates) == len(shifttimes)
        size = len(shiftmonths)
        if argv2 == 'daily':
            size = 1; # only get first element out of each list
        for i in range(0,size):
            print(shiftmonths[i].text.strip() + " " + shiftdates[i].text + ": " + shifttimes[i].text)
    return

def main():
    argv1 = ''
    argv2 = ''
    if len(sys.argv) < 3: #default params if no commandline args
        (argv1, argv2) = ('all', 'weekly')
    else:
        (argv1, argv2) = (sys.argv[1], sys.argv[2])
    if not validate_input(argv1, argv2):
        quit()
    url = 'https://www.humanity.com'
    driver = user_login(url)
    try:
        get_work_schedule(argv1, argv2, url, driver)
    finally:
        driver.close()

if __name__ == "__main__":
    main()
