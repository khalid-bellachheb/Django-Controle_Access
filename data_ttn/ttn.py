import requests
import json

endpoint = 'http://eu.thethings.network:8084/applications/pre2020/devices'
accessKey = 'ttn-account-v2.QgWpB8kKKfhXnndMVKweVz2YKlu3hu-vTU_00-zNRmE'
key = f'Key {accessKey}'

params = {"lorawan_device": {
           "dev_id": "stm32", 
           "dev_eui": "343137325E367E0D", 
           "app_key": "0670530270E403D0FA0BC00708F06F07", 
           "app_eui": "70B3D57ED0034E36",
           "app_id": "pre2020", 
           "dev_addr": "260164BD",
           "activation_constraints": "local", 
           "uses32_bit_f_cnt": True}, 
         "app_id": "pre2020", 
         "dev_id": "stm32"}
        
     
params_json = json.dumps(params)
print(params_json)
response = requests.get(endpoint,headers={'Authorization': key}, params = params_json)

data = response.json()

print(response.status_code)
print(data)
# chellaoui.zakaria@gmail.com
# Azerty1997