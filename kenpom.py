from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import time

chromedriver = '/Users/croper/Downloads/chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.kenpom.com')

username = driver.find_element_by_name('email')
username.send_keys('croper@alumni.nd.edu')

password = driver.find_element_by_name('password')
password.send_keys('byucougars')

form = driver.find_element_by_name('submit')
form.submit()

table = driver.find_element_by_id('ratings-table')
subTables = table.find_elements_by_tag_name("tbody")

for subTable in subTables:
	try:
		# time.sleep(3)
		print "subtable loop"
		rows = subTable.find_elements_by_tag_name("tr")
	except StaleElementReferenceException:
		pass
	for row in rows:
		print "row loop"
		tdElement = row.find_element_by_tag_name("td")
		print tdElement.text
		try:
			# time.sleep(3)
			print "find school try"
			school = row.find_element_by_tag_name("a")
			print school.text
			link = row.find_element_by_link_text(school.text)
			link.click()
		except StaleElementReferenceException:
			print "find school fail"
			pass
		try:
			# time.sleep(3)
			print "find next game try"
			nextGame = driver.find_element_by_name("un")
			# print nextGame.text
			nextGameElements = nextGame.find_elements_by_tag_name("td")[4]
			score = nextGameElements.find_element_by_tag_name("a")
			print school.text, score.text
			driver.back()
		except (NoSuchElementException, StaleElementReferenceException):
			print "find next game fail"
			pass
		driver.back()
