import pandas as pd 
import requests
from datetime import datetime
import datetime
import json
import config

# Using the Yelp API to load business information
token = config.token
current_day = datetime.datetime.now()
url = "https://api.yelp.com/v3/businesses/Pb5WVn8D5Xj26zpc9PutUw/reviews?limit=20&sort_by=yelp_sort"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer {token}".format(token=token)
}
response = requests.get(url, headers=headers)


# Create dataframe from result
data = response.json()
business_id = []
rating = []
time_created = []

for review in data['businesses']:
    business_id.append(review['id'])


business_dic = {
    'business_id': business_id,

    'update_timestamp': current_day
}

col = [ 
    'business_id', 

    'update_timestamp'
]
business_df = pd.DataFrame(business_dic, columns = col)
# print(business_df)