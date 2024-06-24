from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"Message": "Hello from Flask!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
