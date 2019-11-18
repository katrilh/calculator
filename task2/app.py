import json

from calcfile import calculate_expr
from flask import abort, Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def index():
    return "<h3>Welcome to this calculator!</h3>" \
           "</br>Enter a new expression by making a POST request to /calc" \
           "</br>To view the history, make a GET request to /history " \
           "</br>To view a specific entry, make a GET request to /history/<'id'> "


@app.route('/calc', methods=['POST'])
def post_expression(fname='calc.json'):
    if not request.json or 'expression' not in request.json:
        abort(400, "Something went wrong!"
                   "\nRemember to include 'expression' as part of the JSON request!")
    
    with open(fname) as json_file:
        obj = json.load(json_file)  # loads json file as a python object for manipulation
    
    _id, expr, res = None, None, None
    try:
        _id = obj['history'][-1]['_id'] + 1
        expr = request.json['expression']
        res = str(calculate_expr(expr))
        
    except (SyntaxError, TypeError):
        abort(400, "Cannot evaluate this expression!")
        
    temp = {
        "_id":        _id,
        "expression": expr,
        "result":     res
        }
    
    obj['history'].append(temp)
    
    with open(fname, 'w') as json_file:  # saves the output
        json.dump(obj, json_file)
    
    return jsonify({'result': res}), 201


@app.route('/history', methods=['GET'])
def get_history(fname='calc.json'):
    with open(fname) as json_file:
        json_data = json.load(json_file)
    return json_data


@app.route('/history/<int:task_id>', methods=['GET'])
def get_one_expr(task_id, fname='calc.json'):
    with open(fname) as json_file:
        data = json.load(json_file)['history']
    
    entry = [e for e in data if e['_id'] == task_id]
    if len(entry) == 0:
        abort(404)
    
    return entry[0]


if __name__ == '__main__':
    app.run(debug=True)
