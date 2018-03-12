import json
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return cors(jsonify({'tasks': tasks}))

@app.route('/todo/cors', methods=['GET'])
def yourMethod():
    dic ={'msg1':'hello', 'msg2':'goodbye'}
    response = jsonify(dic)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/todo/grocery-list', methods=['GET'])
def get_grocery_list():
    grocery_list = [
      { 'id': 0, 'text': 'Beef' },
      { 'id': 1, 'text': 'Pork' },
      { 'id': 2, 'text': 'Chicken' }
    ]
    response = jsonify({'groceryList':grocery_list})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def cors(response):
    return response.headers.add('Access-Control-Allow-Origin', '*')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
