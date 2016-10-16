import json
import ast

data = open('final.json').read()
data = json.loads(data)

struct = {}

for school in data:
	if 'CODIGO' in school:
		sid = school['CODIGO']
		region = school['REGION']
		nivel = school['NIVEL']
		nombre = school['ESCUELA']
		n = []
		struct[str(sid)] = {
			'region': region,
			'nivel': nivel,
			'nombre': nombre
		}
		struct[sid] = school['grades']

print(json.dumps(struct))