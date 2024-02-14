from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mundo!"

@ap.route("/about")
def hello_about(about):
    return "Hola " + name

if __name__ == "__main__":
    app.run(debug=True)


    