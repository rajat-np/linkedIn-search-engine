from flask import Flask, render_template, request, jsonify
from get import get_result
import csv,os


# setting up assets directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

# setting up template directory
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=ASSETS_DIR)



@app.route('/')
def index():
	return render_template('index.html')



@app.route('/results/<query>')
def results2(query):
	#send the query to get query module
	get_result(query)
	#collect the data from csv and render in the template
	ls = []
	with open('temp.csv', 'r') as csvfile:
		reader = csv.reader(csvfile , quotechar = '|')
		for row in reader:
			if row:
				ls.append(row)
	return render_template('results.html', data = ls)


if __name__ == "__main__":
	app.run(debug=True)
