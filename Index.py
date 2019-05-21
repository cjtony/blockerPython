import time

from datetime import datetime as dt

print('******Bienvenido al bloqueador de sitios para Linux******')
print('Bloquea los sitios temporalmente entre el transcurso del tiempo que tu definas, tu hora de entrada y salida del trabajo!')
contin = input('------Introduce si para continuar: ')

accept = 0
relati = 0

if contin == 'si' or contin == 'Si':
	accept = 1

if accept == 1:
	print('Utiliza un formato de 24 horas :D')
	from_hour = input('Introduce tu hora de entrada al trabajo: ')
	to_hour = input('Introduce tu hora de salida del trabajo: ')
	if from_hour != 0 and to_hour != 0:
		relati = 1

if relati == 1:
	host_path_unix = "/etc/hosts"
	#host_dir = 'hosts'
	host_dir = host_path_unix
	redirect = '127.0.0.1'
	websites_list = [
		"www.facebook.com",
		"facebook.com",
		"mail.google.com"
	]
	while True:
		if dt(dt.now().year, dt.now().month, dt.now().day, int(from_hour)) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, int(to_hour)):
			print(' ****** Estado : Trabajando... ******')
			with open(host_dir, 'r+') as file:
				content = file.read()
				for website in websites_list:
					if website in content:
						pass
					else:
						file.write(redirect + " " + website + "\n")
		else:
			print(' ****** Estado :  Libre... ******')
			with open(host_dir, 'r+') as file:
				content = file.readlines()
				file.seek(0)
				for line in content:
					if not any(website in line for website in websites_list):
						file.write(line)
				file.truncate()
		time.sleep(2)