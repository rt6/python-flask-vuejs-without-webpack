import json
from flask import Flask, jsonify, request


notes_list = [
    {
        'id':'1', 
        'text':'lets go shopping'
    },
    {
        'id':'2', 
        'text':'lets go movies'
    }
]

app = Flask(__name__, static_folder='./static')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/test', methods=['GET'])
def test():
    return(jsonify({'msg':'hello'}))


@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if request.method == 'GET': 
        app.logger.info(notes_list)
        return jsonify({'data': notes_list}), 200
    else:
        new_note = json.loads(request.data)['text']
        app.logger.info('POST {}'.format(new_note))
        next_id = len(notes_list) + 1
        notes_list.append({'id': next_id, 'text': new_note})
        app.logger.info('update notes {} '.format(notes_list))
        return jsonify({'msg':'success', 'data':notes_list})


if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
