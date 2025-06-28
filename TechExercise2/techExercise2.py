from flask import Flask
# Create web app
app = Flask(__name__)

# Page where app says hello to user
@app.route('/hello/<name>')
def hello(name):
    return "Hello %s!" % name

# Default hello world page
@app.route("/")
def helloWorld():
    return "Hello World! go to /hello/yourName for more! (yourName is any variable)"
# Main function
if __name__ == "__main__":
    app.run()


# Hello, this is Andrew
