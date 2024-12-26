from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
        return "This is the landing page of the flask app."

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=8100)