from flask import Flask, jsonify, request, abort, send_from_directory
from flask_cors import CORS
import uuid
import os

app = Flask(__name__, static_url_path='')
CORS(app)

tasks = []

def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/script.js')
def script():
    return send_from_directory('', 'script.js')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': str(uuid.uuid4()),
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = find_task(task_id)
    if task:
        return jsonify(task), 200
    else:
        abort(404)

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    task = find_task(task_id)
    if not task:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) is not str:
        abort(400)
    task['title'] = request.json.get('title', task['title'])
    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = find_task(task_id)
    if not task:
        abort(404)
    tasks.remove(task)
    return '', 204

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
