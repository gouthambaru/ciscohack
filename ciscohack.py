import requests
import json
def getTicket():
	url='https://10.1.121.105/api/v1/ticket'
	payload={"username":"admin","password":"Cisco123!"}
	header={"content-type":"application/json"}
	response=requests.post(url,data=json.dumps(payload),headers=header,verify=False)
	print(response.text)
	r_json=response.json()
	ticket=r_json["response"]["serviceTicket"]
	return ticket
def getNetworkDevices(ticket):
	url='https://10.1.121.105/api/v1/host'
	header = {"content-type": "application/json", "X-Auth-Token":ticket}
	response = requests.get(url, headers=header, verify=False)
	print ("Hosts = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	r_json=response.json()
	for i in r_json["response"]:
		print(i["id"]+" "+i["vlanId"])

theTicket=getTicket()
getNetworkDevices(theTicket)
