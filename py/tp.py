from flask import Flask
from flask import send_file
from flask import jsonify
from time import sleep
import json

port = 8000
application = Flask(__name__)


static_dir = './static/files'

resources_file = "./resources.json"

with open(resources_file) as f:
  resource_data = json.load(f)

@application.route("/")
def root():
  return 'Holis'

@application.route("/static/<string:filename>")
def serve_static(filename):
  return send_file('{}/{}'.format(static_dir, filename))

@application.route("/slow")
def slow():
  for x in range(0, 10000):
    a = 4
  return 'For'

@application.route("/resources/<int:resource_id>")
def get_resource(resource_id):
  return jsonify(resource_data[resource_id])

if __name__ == "__main__":
  application.run(host='localhost', port='8000')
