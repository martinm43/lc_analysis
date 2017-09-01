def coord_ip():
	import requests 
	import json 
	send_url = 'http://freegeoip.net/json' 
	r = requests.get(send_url) 
	j = json.loads(r.text) 
	lat = j['latitude'] 
	lon = j['longitude']
	return [lat,lon]


def coord_termux():
	import os
	import json
	termux_location=os.popen('termux-location -p network').read() 
	j = json.loads(termux_location)
	lat = j['latitude'] 
	lon = j['longitude']
	return [lat,lon]

if __name__=="__main__":
    a=coord_ip()
    b=coord_termux_gps()
    print a
    print b
