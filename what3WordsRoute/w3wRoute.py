from bs4 import BeautifulSoup
import urllib2,sys, json
import gpxpy
import gpxpy.gpx

gpxFile = open('aragonese-way.gpx', 'r')
gpx = gpxpy.parse(gpxFile)
ws="https://api.what3words.com/v2/reverse?coords="

#code borrowed from http://www.trackprofiler.com/gpxpy/index.html to extract GPX points
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            lat = str(point.latitude)
            lng = str(point.longitude)
            #website with personal key for what3words API located at https://docs.what3words.com/api/v2/#reverse-url
            sp=BeautifulSoup(urllib2.urlopen(ws + lat +"%2C" + lng + "&key=11MF6OMW&lang=en&format=json&display=minimal").read(),"html5lib")
            dictionaryOfData = json.loads(sp.text);
            print(dictionaryOfData["words"])
            # print 'Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation)


# lat = "40.7681947"
# lng = "-111.8488958"
# lat = sys.argv[1]
# lng = sys.argv[2]
# sp=BeautifulSoup(urllib2.urlopen(ws + lat +"%2C" + lng + "&key=11MF6OMW&lang=en&format=json&display=minimal").read(),"html5lib")
# dictionaryOfData = json.loads(sp.text);
# print(sp.text)
# print(dictionaryOfData["words"])
