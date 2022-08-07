from distutils.log import debug
from flask import Flask, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'startfund999'
CORS(app)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

user_list = []


@app.route('/')
def home():
    return "<h1>Start Fund - Chat App</h1>"


@app.route('/get_user_list')
def get_user_list():
    # client will call this route every 10 seconds to update every connected client
    return jsonify(user_list)


@socketio.on('on_connect')
def on_connect(data):
    # print(data)
    # data['data'] = data['user_name'] + " has joined"
    add_user_to_list(data)
    send(data, broadcast=True)  # broadcasting new username


@socketio.on("message")
def my_message(incomingPayload):
    # print(incomingPayload)
    # outgoingPayload = incomingPayload
    # try:
    #     outgoingPayload['data'] = incomingPayload['user_name'] + " : " + incomingPayload['data']
    # except:
    #     outgoingPayload['data'] = "unknown"
    send(incomingPayload, broadcast=True)  # this will call js


@socketio.on("left")
def leave(incomingPayload):
    incomingPayload['data'] = incomingPayload['user_name'] + " left the chat! "
    send(incomingPayload, broadcast=True)


@socketio.on("join")
def join(data):
    pass


@socketio.on("leave")
def leave(data):
    pass


def add_user_to_list(new_user):
    for x in user_list:
        print(x)
        if x['user_id'] == new_user['user_id']:
            return
    user_list.append({'user_name': new_user['user_name'], 'user_id': new_user['user_id']})


if __name__ == '__main__':
    socketio.run(app, debug=True)
