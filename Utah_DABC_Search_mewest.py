from bs4 import BeautifulSoup
import mechanize
import requests,sys

# def name(arguements): #everything indented is part of it
def beverageSearch(key, num):
    br = mechanize.Browser()
    br.open('https://webapps2.abc.utah.gov/Production/OnlineInventoryQuery/IQ/InventoryQuery.aspx')
    # <input name="ctl00$ContentPlaceHolderBody$tbCscCode" type="text" onchange="javascript:setTimeout('__doPostBack(\'ctl00$ContentPlaceHolderBody$tbCscCode\',\'\')', 0)" onkeypress="if (WebForm_TextBoxKeyHandler(event) == false) return false;" id="ContentPlaceHolderBody_tbCscCode" tabindex="1" class="tbHeight22" title="enter CSC code" style="width:200px;">

    response = br.response()

    br.form = list(br.forms())[0]

    control = br.form.find_control('ctl00$ContentPlaceHolderBody$tbCscCode')

    #021030 - error case | 021602 - works |
    control.value = num #eh taylor small batch #make a dictionary to loop through here

    try:
        page = br.submit();
        #BeautifulSoup to get the data
        #find the tag type and value associated with it
        #Getting the response in beautifulsoup
        soup = BeautifulSoup(page, "html5lib")

        #Get the product name
        nameLine = soup.find("span", {"id":"ContentPlaceHolderBody_lblDesc"})
        name = nameLine.get_text()

        #Get the current price
        priceLine = soup.find("span", {"id":"ContentPlaceHolderBody_lblPrice"})
        price = priceLine.get_text()

        #Find the current amount in warehouses
        warehouseLine = soup.find("span", {"id":"ContentPlaceHolderBody_lblWhsInv"})
        warehouse = warehouseLine.get_text()

        #Find the current amount on order to warehouse
        warehouseOnOrderLine = soup.find("span", {"id":"ContentPlaceHolderBody_lblWhsOnOrder"})
        warehouseOnOrder = warehouseOnOrderLine.get_text()

        #Get the site inventory if it is there
        #surround this with a try catch - try accept block
        table = soup.find( "tr", {"class":"gridViewRow"})
        locationData = table.get_text().replace("\t","").split("\n")

        print 'Product Name: ', name
        print 'Price: ', price
        print 'Warehouse Inventory: ', warehouse
        print 'Current On Order: ', warehouseOnOrder
        print 'Site: ', locationData[1]
        print 'Qty: ', locationData[2].replace(" ","")
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

    except AttributeError:
        #if in a loop, i can continue
        print 'No Product Information Available: ', key
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

#Dictionary of Beverages
whiskies = {"Pappy_10" : '020146', "Pappy_12" : '021906', "Pappy_15" : '020150', "Pappy_20" : '021016',
"Pappy_23" : '021030', "William_Larue_Weller" : '022086', "George_Stagg" : '018416', "Sazerac_18" : '027096',
"Sazerac_Rye_6" : '027100', "EagleRare_17" : '017756', "Thomas_Handy" : '027036', "Stagg_Junior" : '021540',
"EHTaylor_SmallBatch" : '021602', "EHTaylor_SingleBarrell" : '021589', "EHTaylor_BarrelProof" : '021600',
"EHTaylor_StraightRye" : '027101', "EHTaylor_FourGrain" : '021605', "WhistlepigRye_12" : '027145',
"WhistlepigRye_15" : '015320', "ElijahCraig_18" : '017920', "Yamazaki_12" : '015996', "Yamazaki_18" : '015986',
"SuntoryHibiki" : '015960', "HibikiHarmony" : '015980'}

for key, value in whiskies.iteritems():
    beverageSearch(key, value)
