import time
from datetime import datetime as dt

host_path_windows = r"C:\Windows\System32\drivers\etc"
host_path_unix = "/etc/hosts"

host_dir = 'hosts'

#host_dir = host_path_unix

redirect = '# 127.0.0.1'
P
websites_list = [
	"www.facebook.com",
	"facebook.com",
	"mail.google.com"
]

from_hour = 18
to_hour = 21

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
		print('Trabajando')
		with open(host_dir, 'r+') as file:
			content = file.read()
			for website in websites_list:
				if website in content:
					pass
				else:
					file.write(redirect + " " + website + "\n")
	else:
		print('Hola 2')
		with open(host_dir, 'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in websites_list):
					file.write(line)
			file.truncate()
	time.sleep(2)
