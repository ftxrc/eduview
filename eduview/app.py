from sodapy import Socrata
from flask import Flask, request, abort, jsonify, render_template
from requests.exceptions import HTTPError
import json, statistics
import ast

app = Flask(__name__)
app.debug = True
data = Socrata("data.pr.gov", None)

things = open('static/structured.json').read()
things = json.loads(things)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/v1/get_dataset', methods=['GET'])
def get_dataset():
	# Get the set id
	if not request.args.get('id'):
		abort(404)
	
	set_id = request.args.get('id')

	# Can't pass dict. Refactor all this
	limit = None
	region = None
	offset = None
	school_id = None

	if request.args.get('limit', False):
		limit = request.args.get('limit')

	if request.args.get('region', False):
		region = request.args.get('region')

	if request.args.get('offset', False):
		offset = request.args.get('offset')

	# Fetch dataset
	try:
		dataset = data.get(set_id, limit=limit, offset=offset, region=region)
	except HTTPError as h:
		abort(404)

	return jsonify(dataset)

@app.route('/v1/municipalities', methods=['GET'])
def municipalities():
	# Get the set id
	set_id = 'uaij-e68c'

	# Can't pass dict. Refactor all this
	limit = None
	region = None
	offset = None
	mun = None

	if request.args.get('limit', False):
		limit = request.args.get('limit')

	if request.args.get('municipality', False):
		mun = request.args.get('municipality')

	if request.args.get('offset', False):
		offset = request.args.get('offset')

	# Fetch dataset
	try:
		dataset = data.get(set_id, limit=limit, offset=offset)
	except HTTPError as h:
		abort(404)

	if mun:
		try:
			dataset = data.get(set_id, limit=limit, offset=offset, q=mun)

		except HTTPError as h:
			abort(404)

	for item in dataset:
		item['location_1']['human_address'] = ast.literal_eval(item["location_1"]["human_address"])

	return jsonify(dataset)

@app.route('/m/<sid>')
def m(sid):
	limit = None
	region = None
	offset = None
	mun = None
	try:
		dataset = data.get('uaij-e68c', limit=limit, offset=offset, q=sid)
	except HTTPError as h:
		abort(404)

	grad_rates = False
	gpas = []
	for item in dataset:
		if 'gpa' in item:
			gpas.append(float(item['gpa']))

	mn = float(round(statistics.mean(gpas)))

	return render_template("school.html",
		m_n=sid, mean=mn)

def  get_grad_rates(school_id):
	grad_rates = data.get('aysg-wxf9', school_code=school_id, limit=1, final_grad_rate_subgroup="TODOS LOS ESTUDIANTES")
	if not grad_rates:
		return None
	return round(float(grad_rates[0]['final_grad_rate']))

def create_ha(mi):
	return '\'{\\"address\\":\\"\\",\\"city\\":\\"%s\\",\\"state\\":\\"PR\\",\\"zip\\":\\"\\"}\'' % mi
# TODO: Errorhandler