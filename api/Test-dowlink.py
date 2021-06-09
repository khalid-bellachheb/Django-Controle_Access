import requests
import json
import paho.mqtt.client as mqtt

keyId="XOWNDNEVC7KKKPVU64S5TZ3V4LZTZIF4FFT7QZA"
AppEu='pre-2021-lora-rfid'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_log(mqttc,obj,level,buf):
    print("message:" + str(buf))
    print("userdata:" + str(obj))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("1")
client.username_pw_set(AppEu,keyId)
print("2")
client.connect("eu.thethings.network", 1883, 10)
print("3")
while True:
    client.loop()



"""
data={ 
 "dev_id": "stm32-1",
 "port": 2,                
 "confirmed": False,
 "payload_raw": {
    "led": 1
  }
  
}

y = json.dumps(data)
response = requests.post('http://pre0.enib.fr/api/sended', json=y)

print(response.status_code)"""