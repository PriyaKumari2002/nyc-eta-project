from flask import Flask, request, jsonify
import sys
sys.path.append('src')
from predict import predict_rides

app = Flask(__name__)

# home route
@app.route('/')
def home():
    return jsonify({
        'message': 'NYC Ride Demand Prediction API',
        'status': 'running'
    })

# prediction route
@app.route('/predict', methods=['GET'])
def predict():
    # get values from request
    month   = int(request.args.get('month',   4))
    day     = int(request.args.get('day',     1))
    weekday = int(request.args.get('weekday', 0))
    hour    = int(request.args.get('hour',    8))

    # make prediction
    rides = predict_rides(month, day, weekday, hour)

    return jsonify({
        'month':           month,
        'day':             day,
        'weekday':         weekday,
        'hour':            hour,
        'predicted_rides': rides
    })

if __name__ == '__main__':
    app.run(debug=True)