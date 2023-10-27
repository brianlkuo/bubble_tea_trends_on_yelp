import pandas as pd 
import requests
from datetime import datetime
import datetime
import json
import config

# Using the Yelp API to load business information
token = config.token
current_day = datetime.datetime.now()
url = "https://api.yelp.com/v3/businesses/search?location=New%20York%20City&term=Bubble%20Tea&sort_by=best_match&limit=20"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer {token}".format(token=token)
}
response = requests.get(url, headers=headers)

# Create dataframe from result
data = response.json()
business_id = []
business_name = []
business_url = []
rating = []
latitude = []
longitude = []
review_count = []
price = []
city = []
zip_code = []
country = []
state = []

for business in data['businesses']:
    business_id.append(business['id'])
    business_name.append(business['name'])
    business_url.append(business['url'])
    rating.append(business['rating'])
    latitude.append(business['coordinates']['latitude'])
    longitude.append(business['coordinates']['longitude'])
    review_count.append(business['review_count'])
    price.append(business['review_count'])
    city.append(business['location']['city'])
    zip_code.append(business['location']['zip_code'])
    country.append(business['location']['country'])
    state.append(business['location']['state'])

business_dic = {
    'business_id': business_id,
    'business_name': business_name,
    'business_url': business_url,
    'rating': rating,
    'latitude': latitude,
    'longitude': longitude,
    'review_count': review_count,
    'price': price,
    'city': city,
    'zip_code': zip_code,
    'country': country,
    'state': state,
    'update_timestamp': current_day
}

col = [ 
    'business_id', 
    'business_name',
    'business_url',
    'rating',
    'latitude',
    'longitude',
    'review_count',
    'price',
    'city',
    'zip_code',
    'country',
    'state',
    'update_timestamp'
]
business_df = pd.DataFrame(business_dic, columns = col)
# print(business_df)