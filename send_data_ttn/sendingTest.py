import requests,time

headers = {
    'Content-Type': 'application/json',
    'Authorization': '',
}

data = {
  '{ "dev_id": "stm32-1","port": 2,"confirmed": false,"payload_raw": {"led": 1} }'
}


data =({"ts":time.time()})

r = requests.post('https://eu1.cloud.thethings.network/api/v3/as/applications/pre-2021-lora-rfid/webhooks/http-endpoint/devices/stm32-1/down/push', headers=headers, data=data)

print(r.status_code)
print (r.content)