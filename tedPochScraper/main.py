import re
import requests
from bs4 import BeautifulSoup

wx_report = requests.get('https://www.wrh.noaa.gov/slc/forecast/textproduct.php?pil=SFT&sid=UT')
locations = ['Salt Lake City','Blanding','Toole','Ogden','Brigham City','Provo','Logan','Wendover','Park City','Heber','Randolph','Alta','Mirror Lake','Solider Summitt']
souped_wx = BeautifulSoup(wx_report.text, "html.parser")
lines = souped_wx.find_all('br')

def printLocs():
    for loc in locations:
        print(loc)
while(True):
    print("From among these cities...")
    printLocs()
    choice = input("choose a 5 day weather report: ")

    for i in range(0, len(lines)):
        if lines[i].next_sibling != lines[0].next_sibling:
            entry = str(lines[i].next_sibling)
            if entry.find(choice) > 0:
                print(lines[i].next_sibling)
                print(lines[i+1].next_sibling)
                print(lines[i+2].next_sibling)
                print(lines[i+3].next_sibling)
