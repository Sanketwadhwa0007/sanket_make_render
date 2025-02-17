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
# import oauth
from flask import Flask, redirect, url_for
from authlib.integrations.flask_client import OAuth
# import oauthlib
app = Flask(__name__)
app.secret_key = 'your_secret_key'
oauth = OAuth(app)

# Set up Facebook OAuth
facebook = oauth.register(
    'facebook',
    client_id='your_client_id',
    client_secret='your_client_secret',
    authorize_url='https://www.facebook.com/v12.0/dialog/oauth',
    authorize_params=None,
    access_token_url='https://graph.facebook.com/v12.0/oauth/access_token',
    access_token_params=None,
    refresh_token_url=None,
    client_kwargs={'scope': 'email'},
)


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
@app.route("/data/images", methods=["POST"])
def receive_data():
    data = request.json  # Get JSON data
    image_urls = [item["link"] for item in data.get("items", [])]
    return jsonify({"received_data": image_urls})

# Facebook OAuth Callback
@app.route("/auth/facebook", methods=["POST"])
def facebook_login():
    # Redirect the user to Facebook's OAuth authorization page
    redirect_uri = url_for('facebook_callback', _external=True)
    return facebook.authorize_redirect(redirect_uri)

@app.route("/auth/facebook/callback", methods=["POST"])
def facebook_callback():
    token = oauth.facebook.authorize_access_token()
    user_info = oauth.facebook.get("https://graph.facebook.com/me?fields=id,name,email").json()
    return f"Hello, {user_info['name']}!"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
