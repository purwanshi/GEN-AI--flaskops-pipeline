from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
    return "i am lw from india"

@app.route("/phone")
def lwphone():
    return "3465797865"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
