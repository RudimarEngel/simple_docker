from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


# Comandos docker:
# docker build -t test:latest .
# docker run -p 8000:8000 test:latest
# 

