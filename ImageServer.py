from flask import Flask, request, jsonify, send_from_directory
import subprocess
import os

app = Flask(__name__)

IMAGE_DIRECTORY = 'pi'

@app.route('/imageCapture', methods=['GET'])
def call_external_program():
    try:
        result = subprocess.check_output(['python3', 'ImageCapture.py'], universal_newlines=True)
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'error_message': str(e)})


@app.route('/downloadImage', methods=['GET'])
def download_image():
    # Get the filename from the request parameters
    filename = request.args.get('filename')

    # Check if the filename is provided
    if not filename:
        return jsonify({'error': 'Please provide a filename parameter.'})

    # Check if the file exists in the specified directory
    image_path = os.path.join(IMAGE_DIRECTORY, filename)
    if not os.path.exists(image_path):
        return jsonify({'error': 'File not found.'})

    # Send the file for download
    return send_from_directory(IMAGE_DIRECTORY, filename, as_attachment=True)

@app.route('/listImages', methods=['GET'])
def list_files():
    # Get the list of files in the specified directory
    try:
        files = [f for f in os.listdir(IMAGE_DIRECTORY) if os.path.isfile(os.path.join(IMAGE_DIRECTORY, f))]
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': f'Error listing files: {str(e)}'})


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

