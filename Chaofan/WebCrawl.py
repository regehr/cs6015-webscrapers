#!/usr/bin/python
import re
import urllib.request
import json

def InsertDict(D, key, value):
	D.setdefault(key)
	D[key] = value

def GetHtml(url):
	response = urllib.request.urlopen(url)
	text = response.read().decode('gbk')
	return text

def CreateCityDict(str, Dict):
	for i in range(len(str)):
		s = str[i].split('(')
		cityName = s[0]
		cityCode = s[1].replace(')', '')
		InsertDict(Dict, cityName, cityCode)

def GetCityCode(city, Dict):
	for d in Dict:
		if city == d:
			return Dict[d]
		else:
			pass

def GetLowestPriceUrl(departureCityCode, destinationCityCode, date):
	return 'http://flights.ctrip.com/domestic/ajax/Get90DaysLowestPrice?dcity=%s&acity=%s&ddate=%s&searchType=S&r=0.18035678380179632' % (departureCityCode, destinationCityCode, date)

def GetLowestPriceDate(lowestPriceHtml, Dict):
	date = json.loads(lowestPriceHtml)
	dateList = re.findall(r'[0-9]{4}\-[0-9]{2}\-[0-9]{2}', lowestPriceHtml)
	priceList = re.findall(r'\d{3,4}', lowestPriceHtml)
	filterPriceList = []
	min = 500

	for i in range(len(priceList)):
		if int(priceList[i]) == 2017 or int(priceList[i]) == 2018:
			pass
		else:
			filterPriceList.append(priceList[i])
	#construct dict(date, price)
	print('\nStart Searching...')
	for i in range(len(dateList)):
		InsertDict(Dict, dateList[i], filterPriceList[i])
		print('Flight found on %s with price ¥%s' % (dateList[i], filterPriceList[i]))
	#compare the price with min, if < min, then update min
	for d in Dict:
		if int(Dict[d]) < int(min):
			min = Dict[d]
		else:
			pass
	#get date 
	for d in Dict:
		if Dict[d] == min:
			print('\nCheapest flight found is on: %s with price: ¥%s' % (d, Dict[d]))
			return d

if __name__ == "__main__":
	cityName_cityCodeDict = {}
	date_priceDict = {}
	cityCodeUrl = 'http://webresource.c-ctrip.com/code/cquery/resource/address/flight/flight_new_poi_gb2312.js?releaseno=?CR_2018_01_07_22_18_26'
	citycodeHtml = GetHtml(cityCodeUrl)
	cityCodeStr = re.findall(r'[\u4e00-\u9fa5]+\([A-Z]+\)', citycodeHtml)
	CreateCityDict(cityCodeStr, cityName_cityCodeDict)
	departureCity = input('Departure: ')
	destinationCity = input('Destination: ')
	date = input('date: ')
	departureCityCode = GetCityCode(departureCity, cityName_cityCodeDict)
	destinationCityCode = GetCityCode(destinationCity, cityName_cityCodeDict)
	lowestPriceUrl = GetLowestPriceUrl(departureCityCode, destinationCityCode, date)
	lowestPriceHtml = GetHtml(lowestPriceUrl)
	targetDate = GetLowestPriceDate(lowestPriceHtml, date_priceDict)
	targetUrl = 'http://flights.ctrip.com/booking/%s-%s-day-1.html?DDate1=%s' % (departureCityCode, destinationCityCode, targetDate)
	#print(lowestPriceUrl)
	print('Targeted link to the found flight info: ', targetUrl)



