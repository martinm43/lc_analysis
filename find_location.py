#test line. 
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
	#For now network only. They seem to be having issues with h/w
        #6 Sep 2017
	import os
	import json
	termux_location=os.popen('termux-location -p network').read() 
	try:
		j = json.loads(termux_location)
	except ValueError:
		print('No value found for coordinates')
		return
	lat = j['latitude'] 
	lon = j['longitude']
	return [lat,lon]

if __name__=="__main__":
    a=coord_ip()
    b=coord_termux()
    print a
    print b
