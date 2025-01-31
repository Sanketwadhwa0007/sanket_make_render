from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_code():
    # data = request.json  # Get data from Make.com
    result = {"message": "Hello, Make.com!", "received": "data"}
    return jsonify(result)  # Send response

if __name__ == "__main__":
    app.run(debug=True)
