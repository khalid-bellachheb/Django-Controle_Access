import requests
import json

'''
https://curl.trillworks.com/
'''

headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-v2.QgWpB8kKKfhXnndMVKweVz2YKlu3hu-vTU_00-zNRmE',
}

params = (
    ('last', '1m'),
)

response = requests.get('https://pre2020.data.thethingsnetwork.org/api/v2/query/stm32', headers=headers, params=params)

if(str(response)=="<Response [200]>"):
  ## Read the responses into a Pandas Dataframe
  res=response.json()
  for x in res :
    obj=data_ttn(device_id=x["device_id"],badge=x["badge"],Autorisation=x["authorisation"],Porte=x["porte"], Zone=x["zone"])
    obj.save()
  print('ok')
else :
  print("not ok")