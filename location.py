def coord_ip():
	import requests 
	import json 
	send_url = 'http://freegeoip.net/json' 
	r = requests.get(send_url) 
	j = json.loads(r.text) 
	lat = j['latitude'] 
	lon = j['longitude']
	return [lat,lon]

if __name__=="__main__":
    a=coord_ip()
    print a