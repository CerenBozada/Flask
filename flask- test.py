from pymongo import MongoClient
from flask import Flask, request
from bson.json_util import dumps
import json
from bson.objectid import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


client = MongoClient('localhost', 27017)

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")

db = client.flask
posts = db.posts

users = db.users


@app.route("/")
def index():
    post_data = posts.find()
    return dumps(post_data)


@app.route("/new_post")
def new_post():
    posts.insert_one({"name": "Ceren", "career": "programming"})
    return "ok"


@app.route("/create_user", methods=['POST'])
def create_user():
    json = JSONEncoder().encode(request.json)
    users.insert_one(request.json)
    return "ok"


@app.route("/get_users", methods=['GET'])
def get_users():
    user_data = users.find()
    return JSONEncoder().encode(list(user_data))


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(host='
