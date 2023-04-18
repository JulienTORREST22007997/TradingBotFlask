from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Test"

@app.route('/alert', methods=['POST'])
def alert():
    # Extract the symbol and signal from the JSON data
    data = request.json
    symbol = data['symbol']
    signal = data['signal']
    
    # Append the signal to the list of signals
    signals.append({'symbol': symbol, 'signal': signal})

    return 'OK'

@app.route('/signals', methods=['GET'])
def get_signals():
    # Return the signals as a JSON response
    return jsonify(signals)


if __name__ == '__main__':
    signals = []
    app.run(host='0.0.0.0', port=8080)
