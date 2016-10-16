import json
import ast

meta = open('meta.json').read()
meta = json.loads(meta)


directory = open('high.json').read()
directory = json.loads(directory)

new_dataset = directory.copy()

for idx, school in enumerate(directory):
	new_dataset[idx]['grades'] = []
	for data in meta:
		# print(data.keys())
		if school['ESCUELA'] == data.get('school'):
			# Strip useless metadata at this point
			del data['city']
			new_dataset[idx]['grades'].append(data)

print(json.dumps(new_dataset))