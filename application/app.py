from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/swap', methods=['POST'])
def swap():
    try:
        # Check if 'string' parameter is present in the POST request
        if 'string' not in request.form:
            return jsonify({'error': 'Missing parameter: "string"'}), 400

        # Get the value of the 'string' parameter from the POST request
        input = request.form['string']

        # Swap the case of the string
        swapped = input.swapcase()

        # Return the swapped string in the response
        return jsonify({'result': swapped}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
