from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return f"<p>Hello, dear! nice using {user_agent}</p>"

def info():
    return f"<h5>this is first page with custom routing</h5>"

def custom_routes():
    app.add_url_rule('/info', 'info', info)

if __name__ == '__main__':
    custom_routes()
    app.run(debug=True)