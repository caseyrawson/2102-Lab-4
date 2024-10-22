from flask import Flask, request

app = Flask(__name__)

users = {
   "Casey": "school",
   "Phil": "school1"
}

@app.route("/")
def hello():
   return "You called?"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/login", methods=['POST'])
def login():
    id = request.form['id']
    token = request.form['token']

    if not id or not token:
       return "Incorrect Login"
    if id in users and users[id] == token:
       return "Welcome " + id
    else:
       return "Incorrect Login"

if __name__ == "__main__":
   app.run(host='0.0.0.0')