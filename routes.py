@app.route('/', methods=[ 'GET' ])
def home():
    return """
        <h1>Babby's Home Page</h1>
        <p>Welcome to Babby's first API!</p>
    """

@app.route('/api/v1/resources/babbys', methods=[ 'GET' ])
def index():
    return jsonify(babbys)

@app.route('/api/v1/resources/babbys/<id>', methods=[ 'GET' ])
def show(id):
    result = None

    for babby in babbys:
        if babby['id'] == int(id):
            result = babby
    
    if result is None:
        return jsonify('no babby was found')
    else:
        return jsonify(result)