#File: moab.py
#To run in terminal: python moab.py trail (need single quotes around multiple word trail name)
import sys, urllib2, datetime
trail = sys.argv[1] #trail name is input as a command line argument
print "" #for formatting in terminal

#jeep trail info is pulled from alltrails.com (except trailhead coordinates - utah.com)
#Metal Masher, Pritchett Canyon, Poison Spider, Moab Rim, Behind the Rocks
if trail == 'Metal Masher' or trail == 'metal masher' or trail == 'masher':
    print "Trail chosen: Metal Masher (38.60851, -109.70375)"
    html = urllib2.urlopen('https://www.alltrails.com/trail/us/utah/metal-masher-4x4-trail')
elif trail == 'Pritchett Canyon' or trail == 'pritchett canyon' or trail == 'pritchett':
    print "Trail chosen: Pritchett Canyon (38.53523, -109.59979)"
    html = urllib2.urlopen('https://www.alltrails.com/trail/us/utah/pritchett-canyon-4x4-trail')
elif trail == 'Poison Spider' or trail == 'poison spider' or trail == 'spider':
    print "Trail chosen: Poison Spider Mesa (38.53304, -109.60784)"
    html = urllib2.urlopen('https://www.alltrails.com/trail/us/utah/poison-spider-mesa-trail')
elif trail == 'Moab Rim' or trail == 'moab rim' or trail == 'rim':
    print "Trail chosen: Moab Rim (38.5589, -109.58304)"
    html = urllib2.urlopen('https://www.alltrails.com/trail/us/utah/moab-rim-trail')
elif trail == 'Behind the Rocks' or trail == 'behind the rocks' or trail == 'rocks':
    print "Trail chosen: Behind the Rocks (38.44045, -109.42984)"
    html = urllib2.urlopen('https://www.alltrails.com/trail/us/utah/behind-the-rocks-4x4-trail')
else:
    print("Incorrect trail entered. Enter masher, pritchett, spider, rim, or rocks.")
    print "" #for formatting in terminal
    sys.exit() #exit program if incorrect trail is provided

#used for pulling info for each trail
ratingTag = 'Rating: '
distTag = '<div class="stats-label">DISTANCE</div>'
elevTag = '<div class="stats-label">ELEVATION GAIN</div>'
routeTypeTag = '<div class="stats-label">ROUTE TYPE</div>'
for line in html: #loop through each line in trail html file
    if ratingTag in line:
        rating = html.next()
        rating = html.next()
        break
for line in html: #loop through each line in trail html file
    if distTag in line:
        distance = (html.next())[35:-7] #find distance as substring in html
    if elevTag in line:
        elevation = (html.next())[35:-7] #find elevation gain as substring in html
    if routeTypeTag in line:
        routeType = (html.next())[33:-7] #find route type as substring in html
        if routeType == 'Out &amp; Back':
            routeType = "Out & Back"
html.close() #close trail info html file

#obtain today's date
date = datetime.datetime.today().strftime("%m-%d-%Y")

#find current temp in Moab using the National Weather Service webpage
moabTempHTML = urllib2.urlopen('https://forecast.weather.gov/MapClick.php?lat=38.573270000000036&lon=-109.54965999999996#.Wpg0CpPwa8U')
currentTempTag = '<p class="myforecast-current-lrg">' #look for this tag to find the current temperature
for line in moabTempHTML: #loops through each line in the html from the webpage
    if currentTempTag in line: #looks for the tag in each line
        temp = line[40:-11]
        break
moabTempHTML.close() #close the file

#find the forecast for the day using wunderground.com
moabForecastHTML = urllib2.urlopen('https://www.wunderground.com/weather/us/ut/moab?cm_ven=localwx_today')
hiloTag = 'class="hi-lo">'
precipTag = '% Precip.'
for line in moabForecastHTML:
    if hiloTag in line:
        highTemp = line[80:-112]
        lowTemp = line[178:-14]
    if precipTag in line:
        precipitation = line[44::]
moabForecastHTML.close()

print ""
print "Distance:", distance
print "Elevation gain:", elevation
print "Route type:", routeType
print "Rating:", rating
print "Today's date:", date #print current date in mm-dd-yyyy
print "The current temperature in Moab is:", temp, "F" #print current temp in Moab
print "The forecast for Moab today is:"
print "     High:", highTemp, "F"
print "     Low:", lowTemp, "F"
print "     Precipitation:", precipitation
