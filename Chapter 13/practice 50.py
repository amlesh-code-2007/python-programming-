# Expole the 'flask' module and create a web server using flask and puthon.......

from flask import Flask

app = Flask(__name__)

@app.route ("/")
def Hello_World():
    return "<p>Hello, World! </p>"

app.run()