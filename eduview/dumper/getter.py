import requests
import time
import json
from sodapy import Socrata

count = 1000
students = requests.get('https://data.pr.gov/resource/uaij-e68c.json?$offset=0').json()

while True:
	sets = requests.get('https://data.pr.gov/resource/uaij-e68c.json?$offset=%s' % count).json()
	count = count + 1000
	time.sleep(1)
	if sets == []:
		break
	else:
		students.append(sets)
print(json.dumps(students))

