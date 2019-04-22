from geocode import getGeocodeLocation
import httplib2 , json 

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "V5IECCKPKE4WHFC4GMOHASD240DBY0ZVJICDKXJUDSHNEYU1"
foursquare_client_secret = "W1YKHE514OBW1RA4LUUDFXSOY01MWL2UVHGM4MZX5LYGHNV1"
foursquare_version = "20190421"


def  findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
    latitude,longitude = getGeocodeLocation(location)
    print((latitude,longitude))
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
    
    url1 = ("https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=%s" % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType,foursquare_version))
    h1 = httplib2.Http()
    response1 , content1 = h1.request(url1,'GET')
    result1 = json.loads(content1)
    #print "response header: %s \n \n " % response1

    #3. Grab the first restaurant
    if result1['response']['venues']:
        restaurant = result1['response']['venues'][0]
        restaurant_name = result1['response']['venues'][0]['name']
        venue_id = restaurant['id']
        restaurant_address = restaurant['location']['formattedAddress']
        address = ""
        for i in restaurant_address:
            address +=  i + " "
        restaurant_address = address

        #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        # Use foursquare API to find the picture
        url2 = ("https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=%s" % (venue_id ,foursquare_client_id, foursquare_client_secret,foursquare_version) )
        h2 = httplib2.Http()
        response2 , content2 = h2.request(url2,'GET')
        result2 = json.loads(content2)
        print "response header: %s \n \n " % response2

        if result2['response']['photos']['items']:
            #5. Grab the first image 
            image = result2['response']['photos']['items'][0]
            image_prefix = image['prefix']
            image_suffix = image['suffix']
            imageAddress = image_prefix + "300x300" +image_suffix
        else:
            #6. If no image is available, insert default a image url
            imageAddress = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"  
        
        #7. Return a dictionary containing the restaurant name, address, and image url
        restaurantInfo = {'name':restaurant_name,'address':restaurant_address,'imageUrl':imageAddress}
        # print result 
        print "Resturant Name : %s" % restaurantInfo['name']
        print "Resturant Address: %s" % restaurantInfo['address']
        print "Image : %s" % restaurantInfo['imageUrl']
        print("\n")
        return restaurantInfo
    else:
        
        print("Resturant not found for %s location " % (location))
        return "Resturant not found"


if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney, Australia")