from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import getpass;

# cap = DesiredCapabilities().FIREFOX
# cap["marionette"] = False

email = raw_input("Enter Email")
pswd = getpass.getpass()# this prompts for a password

driver = webdriver.Firefox()

#driver = webdriver.Firefox(capabilities=cap, executable_path='/usr/local/bin/geckodriver')
driver.get("https://www.linkedin.com")
# assert "linkedin" in driver.title
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
searchForm[0].send_keys("David Bean")
searchForm[0].send_keys(Keys.RETURN)
time.sleep(5)
#get the first search result
entries = driver.find_elements_by_class_name("name-and-icon")
entries[0].click()

print driver.title

elements = driver.find_elements_by_xpath('//ul/li/div/div')
print("Elements:")
print(len(elements))
counter = 0;
for each in elements:
    print(each.get_attribute('class'))

    textSection = each.find_element_by_class_name("pv-entity__description Sans-15px-black-70% mt4")
    html = textSection.get_attribute('innerHTML')
    print html
    print counter
    counter += 1
    # except:
    #     print("bad node")
    #     print(each.getattribute('innerHTML'));
print("the end")

# driver.quit()
