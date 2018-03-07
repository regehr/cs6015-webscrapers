from bs4 import BeautifulSoup
import urllib2,sys
ws="https://forecast.weather.gov/MapClick.php?lat="
ls={"SLC":ws+"40.7835&lon=-111.9807#.WpcXS2aZNQI",
    "ORL":ws+"25.9275&lon=-80.2232#.WpcXLWaZNQI",
    "BUR":ws+"44.4759&lon=-73.2128#.WpcXbWaZNQI",
    "HON":ws+"21.4395&lon=-157.9436#.WpdzImaZNQI",
    "HOU":ws+"29.7606&lon=-95.3697#.WpdzuGaZNQI"}
sp=BeautifulSoup(urllib2.urlopen(ls[sys.argv[1]]).read(),"html5lib")
print(sp.find("p",class_="myforecast-current-lrg").text)
