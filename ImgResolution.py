from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/setResolution', methods=['GET'])
def setResolution():
    # Get parameters from the request
    param1 = request.args.get('resolution')

    # Validate parameters (optional)
    if param1 is None:
        return jsonify({'error': 'Missing parameters'}), 400

    # Process parameters (you can perform any logic here)
    result = param1
    filename = 'resolution.txt'
    with open(filename, 'w') as f:
        f.write(result)
    f.close()

    with open(filename, "r") as file:
        data = file.read()
        result = data
        print(data)

    # Return the result as JSON
    return jsonify({'resolutionValue': result})

@app.route('/getResolution', methods=['GET'])
def getResolution():
    filename = 'resolution.txt'
    with open(filename, "r") as file:
        data = file.read()
        result = data
        print(data)

    # Return the result as JSON
    return jsonify({'resolutionValue': result})
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)

