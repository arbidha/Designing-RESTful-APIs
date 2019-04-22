import httplib2 , json 

def getGeocodeLocation(inputString):
    google_api_key = "your_api_key"
    locationString = inputString.replace(" ","+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?&address=%s&key=%s'% (locationString,google_api_key))
   
    h = httplib2.Http()
    response , content = h.request(url,'GET')
    result = json.loads(content)

    #print response
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    #print "response header: %s \n \n " % response

    #url1 = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=sushi&v=20190421" % (foursquare_client_id, foursquare_client_secret,latitude,longitude))
    #h1 = httplib2.Http()
    #response1 , content1 = h1.request(url1,'GET')
    #result1 = json.loads(content1)

    #print "response header: %s \n \n " % response1
    #return result1
    return (latitude,longitude)
