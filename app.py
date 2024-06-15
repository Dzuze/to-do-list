from flask import Flask, jsonify, request, abort
import uuid
app = Flask(__name__)


tasks = []