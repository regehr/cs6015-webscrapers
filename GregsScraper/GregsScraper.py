# -*- coding: utf8 -*-
# encoding=utf8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass;
from bs4 import BeautifulSoup as bs;
import requests;
import string
from string import maketrans   # Required to call maketrans function.
import stringOperations as SO

#set up the word dictionary
fileName = '/Users/gregorycolledge/gcolledge/WebScraperAssignment/cs6015-webscrapers/GregsScraper/wordUse.txt'
wordCount = dict()
dictionary = open(fileName, 'r')
line = dictionary.readline()
print "--------------- Old STUFF--------------"
print line
while(line != ""):
    tabPos = -1#set to an impossible value
    counter = 0
    for each in line:
        if each == '\n':
            break
        elif each == '\t':
            tabPos = counter
        counter += 1
    wordCount[line[0:tabPos]] = int(line[(tabPos+1):counter])
    line = dictionary.readline()
    print line
    print counter
    print tabPos
dictionary.close()
print len(wordCount)
for each in wordCount:
    print((each) + '\t' + str(wordCount[each]))

email = 'skitch04@gmail.com'
pswd = 'wonderland'

driver = webdriver.Firefox()

driver.get("https://www.linkedin.com")
elem = driver.find_element_by_name("session_key")
elem2 = driver.find_element_by_name("session_password")
elem.clear()
elem2.clear()
elem.send_keys(email)
elem2.send_keys(pswd)
elem2.send_keys(Keys.RETURN)
assert "LinkedIn" in driver.title
time.sleep(5)
#find the search bar
searchForm = driver.find_elements_by_tag_name('input')
searchForm[0].click()
time.sleep(5)
# Enter the name into the search bar
searchForm[0].send_keys("Rachael Stone")
searchForm[0].send_keys(Keys.RETURN)
time.sleep(5)
#get the first search result
entries = driver.find_elements_by_class_name("name-and-icon")
entries[0].click()
time.sleep(5)
buttons = driver.find_elements_by_tag_name('button')
for each in buttons:
    if "Show more" in each.text:
        try:
            each.click();
        except:
            print "unpushable button"
temp = driver.find_element_by_class_name('pv-top-card-section__body')
textsIWant = temp.find_elements_by_xpath('//div/p')
textIWant = textsIWant[0]
for each in textsIWant:
    if(each.get_attribute('class')=='pv-top-card-section__summary-text text-align-left mt4 pt4 ember-view'):
        textIWant = each
print("value: " + str(textIWant.get_attribute('value')))
print("id: " + str(textIWant.get_attribute('id')))
print("class: " + str(textIWant.get_attribute('class')))

soup = bs(textIWant.text, 'lxml')
text = (soup.p.get_text()).lower()#gets the text from the p tag in  soup and makes it all lowercase

textList = (SO.puncRemove(text).split())#removes punctuation and creates a list of words
counter = 0
for each in textList:
    counter += 1
    if each in wordCount:
        wordCount[each] += 1
    else:
        wordCount[each] = 1
print "--------------- NEW STUFF--------------"
newDictionary = open(fileName, 'w+')

for each in wordCount:
    print((each) + ' ' + str(wordCount[each]))
    #The line below writes to the file and also replaces a few rogue symbols (bullets and apostrophes) along the way
    newDictionary.write((each.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\u274b','').replace(u'\u2022','').replace(u'\u2013','')) + '\t' + str(wordCount[each]) + '\n')

print("the end")
dictionary.close()
driver.quit()
