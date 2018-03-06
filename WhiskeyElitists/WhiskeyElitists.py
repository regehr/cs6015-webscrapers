import sys, mechanize
from bs4 import BeautifulSoup
def whiskeyCheck(key, value):
    br = mechanize.Browser()
    br.open('https://webapps2.abc.utah.gov/Production/OnlineInventoryQuery/IQ/InventoryQuery.aspx')

    response = br.response()
    # 'ctl00$ContentPlaceHolderBody$tbCscCode'
    # br.select_form(form1).set_all_readonly(False)
    br.form = list(br.forms())[0] # form is unnamed
    # for control in br.form.controls:
    #     print control
    # for form in br.forms():
    #     print "Form name: ", form.name
    #     print form
    control = br.form.find_control('ctl00$ContentPlaceHolderBody$tbCscCode')

    control.value = value
    response = br.submit()
    soup = BeautifulSoup(response, "html5lib")
    bottlesInWarehouse = soup.find("span", {"id": "ContentPlaceHolderBody_lblWhsInv"})
    inWarehouse = bottlesInWarehouse.get_text()
    bottlesOnOrder = soup.find("span", {"id": "ContentPlaceHolderBody_lblWhsOnOrder"})
    onOrder = bottlesOnOrder.get_text()
    print "The number of bottles of " + key + " in the warehouse are: " + inWarehouse
    print "The number of bottles of " + key + " on order are: " + onOrder
    if (inWarehouse != "0" or onOrder != "0"):
        location = soup.find("table", {"id": "ContentPlaceHolderBody_gvInventoryDetails"})
        place = location.get_text()
        print "They can be found at: " + place


pappy10 = "Pappy 10 Year"
pappy12 = "Pappy 12 Year"
pappy15 = "Pappy 15 Year"
pappy20 = "Pappy 20 Year"
pappy23 = "Pappy 23 Year"
billLarue = "William Larue Weller"
georgeTStagg = "George T Stagg"
saz18 = "Sazerac 18 Year"
eagleRare17 = "Eagle Rare 17 Year"
thomHandy = "Thomas Handy"
staggJr = "Stagg Junior"
sazRye6 = "Sazerac Rye 6 Year"
ehTSmallBatch = "E H Taylor Small Batch"
ehTSingleBarrell = "E H Taylor Single Barrel"
ehTBarrelProof = "E H Taylor Barrel Proof"
ehTStraightRye = "E H Taylor Straight Rye"
ehTFourGrain = "E H Taylor Four Grain"
whistlePig12 = "Whistlepig Rye 12 Year"
whistlePig15 = "Whistlepig Rye 15 Year"
elijah18 = "Elijah Craig 18 Year"
yamazaki12 = "Yamazaki 12 Year"
yamazaki18 = "Yamazaki 18 Year"
suntoryHibiki = "Suntory Hibiki"
hibikiHarmony = "Hibiki Harmony"
whiskeyDic = {pappy10: "020146", pappy12: "021906", pappy15: "020150", pappy20: "021016", pappy23: "021030",
billLarue: "022086", georgeTStagg: "018416", eagleRare17: "017756", thomHandy: "027036", staggJr: "021540",
sazRye6: "027100", ehTSmallBatch: "021602", ehTBarrelProof: "021600", ehTSingleBarrell: "021589", ehTStraightRye: "027101",
ehTFourGrain: "021605", whistlePig12: "027145", whistlePig15: "015320", elijah18: "017920", yamazaki12: "015996",
yamazaki18: "015986", suntoryHibiki: "015960", hibikiHarmony: "015980"}
for key, value in whiskeyDic.iteritems():
    # print "Key is: " + key + " Value is: " +value
    try:
        whiskeyCheck(key, value)
    except AttributeError:
        continue


# print response.read()
# print response.geturl() # url of the site we just opened
# print response.info() # headers of html
# print response.read() # body of html
