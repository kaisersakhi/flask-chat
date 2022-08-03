from flask import Flask
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'startfund999'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/')
def home():
    return "<h1>Start Fund - Chat App</h1>"


@socketio.on('on_connect')
def on_connect(data):
    # print(data)
    send(data) #broadcasting new username


# @socketio.on('message')  # here the 'message' will specify
# def handle_message(msg):  # will get called on each receive
#     print(msg)
#     # send(msg, broadcast=True)  # get the message and broadcast it back to every client connected


@socketio.on("message")
def my_message(msg):
    print(msg)
    send(msg, broadcast = True) #this will call js 


if __name__ == '__main__':
    socketio.run(app)
