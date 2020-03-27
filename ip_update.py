import urllib2
import json
import time
import subprocess

#can put this in /etc/rc.local

while True:
	try:
		my_public_ip_str = urllib2.urlopen("http://icanhazip.com/").read()
		print my_public_ip_str

		local_ip_request = subprocess.Popen(['hostname', '-I'], stdout=subprocess.PIPE)
		my_local_ip_str, irrelevant = local_ip_request.communicate()
		print my_local_ip_str

		my_ip = {}
		my_ip['value1'] = my_public_ip_str
		my_ip['value2'] = my_local_ip_str
		my_ip = json.dumps(my_ip)

		post_ip = urllib2.Request("https://maker.ifttt.com/trigger/pi_ip/with/key/b1SgHiGpXqazCsnAuVwLi", my_ip, {'Content-Type': 'application/json'})
		post_ip = urllib2.urlopen(post_ip).read()

		print post_ip

		time.sleep(3600)
	except Exception, e:
		print e