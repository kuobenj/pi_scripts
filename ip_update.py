import urllib2
import json

my_ip_str = urllib2.urlopen("http://icanhazip.com/").read()

print my_ip_str

my_ip = {}
my_ip['value1'] = my_ip_str
my_ip = json.dumps(my_ip)

post_ip = urllib2.Request("https://maker.ifttt.com/trigger/pi_ip/with/key/b1SgHiGpXqazCsnAuVwLi", my_ip, {'Content-Type': 'application/json'})
post_ip = urllib2.urlopen(post_ip).read()

print post_ip