import json
import ast
from sodapy import Socrata

directory = open('high.json').read()
directory = json.loads(directory)

students = open('full_json.json').read()
students = json.loads(students)


combined_dataset = []

# Fine tune
results_directory = {}

for student in students:
	if 'igs' in student and 'gpa' in student:
		human_address = ast.literal_eval(student["location_1"]["human_address"])
		for school in directory:
			if human_address['city'] == school["DIRECCION_FISICA_PUEBLO"]:
				# print(student)
				data = {}
				data['city'] = human_address['city']
				data['school'] = student['institucion_de_procedencia'][8:]
				data['igs'] = student["igs"]
				data['gpa'] = student["gpa"]
				#data['gender'] = student["genero"]
				combined_dataset.append(data)

print(json.dumps(combined_dataset))