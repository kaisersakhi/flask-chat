from flask import Flask
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'startfund999'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')  # here the 'message' will specify
def handle_message(msg):  # will get called on each receive
    print(msg)
    send(msg, broadcast=True)  # get the message and broadcast it back to every client connected


if __name__ == '__main__':
    socketio.run(app, debug=True)
