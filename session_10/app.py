from flask import Flask

app = Flask('My Application')

def read_file(filename):
    f = open(filename)
    text = f.read()
    f.close()
    return text


@app.route("/")
def whatever():
    return read_file("index.html")

app.run()
