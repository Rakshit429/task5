from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

@app.route('/first', methods=['GET'])
def first():
    response = make_response(jsonify({"message": "Success"}), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'  # Consider removing hardcoded token
    return response

@app.route('/second', methods=['GET'])
def second():
    # If this is an error response, return an error message
    response = make_response(jsonify({
        "error": "Invalid parameters",
        "param1": "value1",
        "param2": "value2"
    }), 400)
    
    response.headers['Content-Type'] = 'application/json'
    response.headers['Authorization'] = 'Bearer token123'  # Consider removing hardcoded token
    return response

# Global Error Handler
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error": "Bad request"}), 400)

if __name__ == '__main__':
    app.run(debug=True)
