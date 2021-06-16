import requests,json
'''
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer HG26O4CZYQFL7QQZ35ITSB6STD733Q3BGZ7VDNA',
}



data = {

  "webhook": {},
  "field_mask": {},


}

d=json.dumps(data)


r = requests.post('https://eu1.cloud.thethings.network/api/v3/as/webhooks/http-endpoint.stm32-1', headers=headers, data=data)

print(r.status_code)
print (r.content)'''

headers = {
    'Authorization': 'Bearer NNSXS.HG26O4CZYQFL7QQZ35ITSB6STD733Q3BGZ7VDNA',
    'Content-Type': 'application/json',
    'User-Agent': 'my-integration/my-integration-version',
}

data = {
  '{ "downlinks": [{ "frm_payload": "vu8': '", "f_port": 42, }] }'
}

response = requests.post('https://eu1.cloud.thethings.network/api/v3/as/applications/pre-2021-lora-rfid/devices/stm32-1/down/push', headers=headers, data=data)


print(response.status_code)
print (response.content)