import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config[ "DEBUG" ] = True

babbys = [
    {
        'id': 0,
        'babby': 'Babby',
        'dob': '12/12/2020',
        'chonk': True
    },
    {
        'id': 1,
        'babby': 'Bobby',
        'dob': '11/24/2020',
        'chonk': True
    },
    {
        'id': 2,
        'babby': 'Bebbe',
        'dob': '12/29/2020',
        'chonk': True
    }
]

@app.route('/', methods=[ 'GET' ])
def home():
    return """
        <h1>Babby's Home Page</h1>
        <p>Welcome to Babby's first API!</p>
    """

@app.route('/api/v1/resources/babbys/all', methods=[ 'GET' ])
def api_all():
    return jsonify(babbys)

@app.route('/api/v1/resources/babbys', methods=[ 'GET' ])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id field provided. Please specify an id.'

    results = []

    for babby in babbys:
        if babby['id'] == id:
            results.append(babby)

    return jsonify(results)

app.run()