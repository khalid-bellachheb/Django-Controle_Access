import requests,json

url = 'http://pre0.enib.fr/api/matricule'

matricule = "bm-333-jk"
Badge = "1"

data = {
  "matricule_id": matricule,
  "Badge": Badge,
}

d=json.dumps(data)

r = requests.post(url,  verify=False, json=d)
print(type(r))
print(r.status_code)