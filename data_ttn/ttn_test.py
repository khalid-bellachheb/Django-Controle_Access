import requests
import json
import pandas as pd

'''
https://curl.trillworks.com/
'''

headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-v2.QgWpB8kKKfhXnndMVKweVz2YKlu3hu-vTU_00-zNRmE',
}

response = requests.get('https://pre2020.data.thethingsnetwork.org/api/v2/query', headers=headers)


## Read the responses into a Pandas Dataframe
res=response.json()
## Raw DataFrame from TTN Swagger API
df = pd.DataFrame.from_dict(res)
