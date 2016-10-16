import json
import ast
from statistics import mean

directory = open('directory_custom.json').read()
directory = json.loads(directory)

for school in directory:
	results = {}
	gpa_list = list()
	igs_list = list()
	for item in school['grades']:
		gpa_list.append(item['gpa'])
		igs_list.append(item['igs'])
	school['gpa_mean_total'] = mean(gpa_list)
	school['igs_mean_total'] = mean(igs_list)
	print(gpa_list)
	print(igs_list)
