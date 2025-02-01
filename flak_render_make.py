# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route("/", methods=["POST"])
# def run_code():
#     try:
#         print("Headers:", request.headers)  # Debugging
#         print("Raw Data:", request.data)    # Debugging
        
#         data = request.get_json()  # Attempt to parse JSON

#         if not data:
#             return jsonify({"error": "Invalid JSON"}), 400

#         return jsonify({"message": "Data received", "data": data})
    
#     except Exception as e:
#         return jsonify({"error": str(e)}), 200

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 1️⃣ File Upload Route
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)  # Save uploaded file

    return jsonify({"message": "File uploaded!", "filename": file.filename})

# 2️⃣ Simple Route
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})

# 3️⃣ JSON Data Route
@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json  # Get JSON data
    return jsonify({"received_data": data})

# Facebook OAuth Callback
@app.route("/auth/facebook/callback")
def facebook_callback():
    token = oauth.facebook.authorize_access_token()
    user_info = oauth.facebook.get("https://graph.facebook.com/me?fields=id,name,email").json()
    return f"Hello, {user_info['name']}!"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
