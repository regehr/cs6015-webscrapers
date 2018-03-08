from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from time import sleep
import codecs



chromedriver = '/Users/croper/Downloads/chromedriver'
vegasDriver = webdriver.Chrome(chromedriver)
vegasUrl = 'http://www.vegasinsider.com/college-basketball/odds/las-vegas/'
vegasDriver.get(vegasUrl)
oddsTable = vegasDriver.find_element_by_class_name('frodds-data-tbl')
table = oddsTable.find_element_by_tag_name('tbody')
oddsRows = table.find_elements_by_tag_name('tr')

for i in range(0, len(oddsRows)):
	# print i
	rowElement = oddsRows[i].find_elements_by_tag_name('td')
	if len(rowElement) > 1:
		teams = rowElement[0].find_elements_by_tag_name('b')
		teamText1 = teams[0].find_element_by_tag_name('a')
		teamText2 = teams[1].find_element_by_tag_name('a')
		print teamText1.text, teamText2.text
		try:
			scoreBox = rowElement[1].find_element_by_tag_name('a')
			new_string = scoreBox.text.encode('ascii',errors='ignore')
			# final_string = new_string + b'.5' * (len(scoreBox.text) - len(new_string))
			print final_string
		except NoSuchElementException:
			print "no line yet"
			pass
		# values = scoreBox.find_elements_by_tag_name('br')

	++i
driver = webdriver.Chrome(chromedriver)
url = 'https://www.kenpom.com'
driver.get(url)

username = driver.find_element_by_name('email')
username.send_keys('croper@alumni.nd.edu')

password = driver.find_element_by_name('password')
password.send_keys('byucougars')

form = driver.find_element_by_name('submit')
form.submit()
# sleep(5)
table = driver.find_element_by_id('ratings-table')
subTables = table.find_elements_by_tag_name("tbody")

for j in range (0, len(subTables)):
	tableTemp = driver.find_element_by_id('ratings-table')
	subTablesTemp = table.find_elements_by_tag_name("tbody")
	# try:
	# 	# time.sleep(3)
	# print "subtable loop"
	rowsTemp = subTablesTemp[j].find_elements_by_tag_name("tr")
	# except StaleElementReferenceException:
	# 	pass
	for i in range(0, len(rowsTemp)):
		tableTemp2 = driver.find_element_by_id('ratings-table')
		subTablesTemp2 = tableTemp2.find_elements_by_tag_name("tbody")
		rowsTemp2 = subTablesTemp2[j].find_elements_by_tag_name("tr")
		# print "row loop"
		# print row.get_attribute("name")
		tdElement = rowsTemp2[i].find_element_by_tag_name("td")
		school = rowsTemp2[i].find_element_by_tag_name("a")
		print school.text
		link = rowsTemp2[i].find_element_by_link_text(school.text)
		link.click()
		# sleep(1)
		try:
			# time.sleep(10)
			# print "find next game try"
			nextGame = driver.find_element_by_class_name("un")
			# print "next game element found"
			# print nextGame.text
			nextGameElements = nextGame.find_elements_by_tag_name("td")
			print "next game score"
			# sleep(5)
			score = nextGameElements[4].find_element_by_tag_name("a")
			# print "next game score"
			print score.text
			driver.execute_script("window.history.go(-1)")
			# sleep(1)
			# time.sleep(10)
			# time.sleep(30)
		except StaleElementReferenceException:
			# print "StaleElementReferenceException"
			pass
			print "no next game"
			driver.execute_script("window.history.go(-1)")
			# sleep(1)
			# time.sleep(10)
		except NoSuchElementException:
			# print "NoSuchElementException"
			pass
			print "no next game"
			driver.execute_script("window.history.go(-1)")
			# sleep(1)
		++i
	++j
		# time.sleep(30)
