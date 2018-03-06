from bs4 import BeautifulSoup
import time, datetime, sys
from multiprocessing import Pool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#include datetime
now = datetime.datetime.now()
currentDate = ''
tripDate = ''
month = now.month
weekTripMonth = month
day = now.day + 7
weekTrip = day + 7
if day > 30:
    month += 1
    day %= 30
    weekTrip %= 30
    month += 1
    if month > 12:
        month %= 12
if weekTrip > 30:
    weekTrip %=30
    weekTripMonth += 1
    if weekTripMonth > 12:
        weekTripMonth %= 12

year = now.year
currentDate += str(month) + "/" + str(day) + "/" + str(year)
tripDate += str(weekTripMonth) + "/" + str(weekTrip) + "/" + str(year)

slc = 'Salt Lake City, UT'

coloradoSpring = 'Colorado Springs, CO'
portland = 'Portland, OR'
newMexico = 'Albuquerque, NM'
eugene = 'Eugene, OR'
bayArea = 'San Diego, CA'
denver = 'Denver, CO'
vegas = 'Las Vegas, NV'
newYork = 'New York, NY (JFK-Kennedy)'
miami = 'Miami, FL (MIA-Miami Intl.)'
newOrleans = 'New Orleans, LA'
boston = 'Boston, MA'


nationalCityList = [bayArea, coloradoSpring, denver, portland, newMexico, eugene, vegas, newYork, miami, newOrleans, boston]

def navigateAlaskaAirlines(gotToCity, seleniumDriver):
    time.sleep(3) #ensure that the page loads before doing anything else
    seleniumDriver.find_element_by_id('oneWay').click()
    seleniumDriver.find_element_by_id('fromCity1').send_keys(slc)
    time.sleep(1)
    seleniumDriver.find_element_by_id('toCity1').send_keys(gotToCity)
    time.sleep(1)
    departureDate = seleniumDriver.find_element_by_id('departureDate1')
    departureDate.clear()
    departureDate.send_keys(currentDate)
    # if !oneWay:
    #     returnDate = seleniumDriver.find_element_by_id('returnDate')
    #     returnDate.clear()
    #     returnDate.send_keys(weekTrip)
    select = Select(seleniumDriver.find_element_by_id('adultCount'))
    select.select_by_visible_text('2 adults')
    time.sleep(1)
    seleniumDriver.find_element_by_id('findFlights').click()
    time.sleep(6) # wait for page to load
    selectLowPrice = Select(seleniumDriver.find_element_by_id('SortBy0'))
    selectLowPrice.select_by_visible_text('Price')
    html = seleniumDriver.page_source
    seleniumDriver.close()
    soup = BeautifulSoup(html, "html5lib")
    cheapestFlight = soup.find(id='flightInfoRow_0_0')
    flightInfo = cheapestFlight.get_text()
    return flightInfo.split()

def printOutInformationAlaska(goThroughFlightInfo, cityGoingTo):
    cost = ''
    flightTime = ''
    count = 0
    foundHours = False
    foundMinues = False
    prev = ''
    stops = ''
    for string in goThroughFlightInfo:
        if string == 'stop':
            stops += prev + ' ' + string
        if 'hours' in string:
            if foundHours == False:
                flightTime += string
                foundHours = True
        if 'minutes' in string:
            if foundMinues == False:
                flightTime += ' ' + string
                foundMinues = True
        if '$' in string:
            count += 1
            if count == 4:
                cost = string
                break
        prev = string
    # result = "\nALASKA AIRLINES: Todays price from " + slc + " to " + cityGoingTo + " is: " + cost + "\nThe Flight Time is: " + flightTime
    print "\nALASKA AIRLINES: The price for: "+ currentDate +" from " + slc + " to " + cityGoingTo + " is: " + cost + "\nThe Flight Time is: " + flightTime
    if stops == '':
        # result = result + "\nThis flight has: 0 stops"
        print "This flight has: 0 stops"
    else:
        # result = result + "\nThis flight has: " + stops
        print "This flight has: " + stops
    # return result

#listOfResults = []
def runAlaskaWithThreads(city):
    seleniumDriver = webdriver.Chrome(executable_path=r'/Users/waldrich/python/chromeDriver')
    seleniumDriver.get('https://www.alaskaair.com/')
    try:
        # listOfResults.append(printOutInformationAlaska(navigateAlaskaAirlines(city, seleniumDriver), city))
        printOutInformationAlaska(navigateAlaskaAirlines(city, seleniumDriver), city)
    except NoSuchElementException:
        seleniumDriver.close()
        # listOfResults.append("Unable to find: " + city + ". Or Website thinks your a robot and you should fix that." )
        print "Unable to find: " + city + ". Or Website thinks your a robot and you should fix that."



pool = Pool(processes=4)
pool.map(runAlaskaWithThreads, nationalCityList)
