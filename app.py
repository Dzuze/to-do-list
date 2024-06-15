from flask import Flask, jsonify, request, abort
import uuid
app = Flask(__name__)


tasks = []
def find_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200
