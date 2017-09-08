from math import radians, cos, sin, asin, sqrt

from flask import Flask, request, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
	param =request.args.get('x')
	print(param)
	return 'hello',200

@app.route('/comp', methods=['POST'])
def list_comprehension():
	data = request.data
	data_dict = json.loads(data)
	data_list = data_dict["list"]
	return json.jsonify([x**2 for x in data_list])

@app.route('/distance', methods=['GET'])
def haversine():
	coordpoint1 = request.args.get('coord1')
	newdata = coordpoint1.split(',')
	lon1 = float(newdata[0])
	lat1 = float(newdata[1])

	coordpoint2 = request.args.get('coord2')
	newdata2 = coordpoint2.split(',')
	lon2 = float(newdata2[0])
	lat2 = float(newdata2[1])
	
    # # # convert decimal degrees to radians
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
	
    # # # haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	
	a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
	c = 2 * asin(sqrt(a))
	r = 6371  # Radius of earth in kilometers. Use 3956 for miles
	
	f = c * r
	print(f)
	return str(f)


