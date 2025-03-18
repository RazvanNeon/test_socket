from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return "Serverul Flask cu WebSocket este în funcțiune!"

@socketio.on('message')
def handle_message(message):
    print('Mesaj primit:', message)
    emit('response', f"Salut x! Ai trimis: {message}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
