from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Placeholder for a method to retrieve live stock data using Breez
def fetch_live_data():
    # Mock live data (replace with Breez integration)
    stock_data = {
        'ticker': 'AAPL',
        'price': 150.00,
        'volume': 3000
    }
    return stock_data

# Background thread for broadcasting live data
def broadcast_stock_data():
    while True:
        # Fetch live stock data (replace this with Breez's real-time API)
        live_data = fetch_live_data()

        # Emit the data through a WebSocket connection
        socketio.emit('stock_update', live_data)
        time.sleep(5)  # Broadcast update every 5 seconds

# Route for rendering the HTML template
@app.route('/')
def index():
    return render_template('index.html')

# Start the background thread when the server starts
@socketio.on('connect')
def on_connect():
    threading.Thread(target=broadcast_stock_data).start()

if __name__ == '__main__':
    socketio.run(app,debug = True)