import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

from geopy.geocoders import ArcGIS as geocoder
geolocator = geocoder()

# twitter urls for single user and friends
TW_URL = 'https://api.twitter.com/1.1/users/show.json'
TW_FRIENDS = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_info(url, request, count):
    """
    Gets all the information from twitter url as json parses it
    :param url: (str) where to send request (should be twitter url)
    :param request: (str) what should be set as screen_name (
    :param count: (str or number) number of answers we want to get (people)
    :return: (dict or list) - all the information, that we got from .json
    """
    print('Sending request to twitter. Person: ' + request, '. Count: ', count)
    url = twurl.augment(url, {'screen_name': request, 'count': str(count)})

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    data = json.loads(data)
    return data


def parse_account(data):
    """
    Gets all the data from a twitter account infromation, that was previously
    requested as json and parsed to python dict / list
    :param data: json, converted to python dict with twitter account info
    :return: dict - with all the useful data from data and a geocoded location
    """
    result = []

    try:
        location = geolocator.geocode(data['location'], timeout=2)
        geocode = (float(location.latitude), float(location.longitude))
    except:
        geocode = (None, None)

    result.append({
        "name" : data["name"],
        "screen_name": data["screen_name"],
        "followers_count": data["followers_count"],
        "friends_count": data["friends_count"],
        "favourites_count": data["favourites_count"],
        "statuses_count": data["statuses_count"],
        "profile_image": data["profile_image_url_https"],
        "location": data["location"],
        "geocode": geocode
    })

    return result