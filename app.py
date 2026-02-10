from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    return jsonify({
        "status": "success",
        "message": f"Thanks {name}, we received your message!"
    })

if __name__ == "__main__":
    app.run(debug=True)
