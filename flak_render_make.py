from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def run_code():
    try:
        print("Headers:", request.headers)  # Debugging
        print("Raw Data:", request.data)    # Debugging
        
        data = request.get_json()  # Attempt to parse JSON

        if not data:
            return jsonify({"error": "Invalid JSON"}), 400

        return jsonify({"message": "Data received", "data": data})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
