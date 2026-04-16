import pickle
import pandas as pd

# load the saved model
def load_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# predict rides for a given time
def predict_rides(month, day, weekday, hour):
    model = load_model()
    
    # create input dataframe
    input_data = pd.DataFrame({
        'month':   [month],
        'day':     [day],
        'weekday': [weekday],
        'hour':    [hour]
    })
    
    # make prediction
    prediction = model.predict(input_data)
    return round(prediction[0])

# test it out
if __name__ == '__main__':
    # predict rides on a Monday at 8am
    rides = predict_rides(month=4, day=15, weekday=0, hour=8)
    print(f"Predicted rides: {rides}")
    
    # predict rides on a Friday night
    rides = predict_rides(month=4, day=18, weekday=4, hour=22)
    print(f"Friday night predicted rides: {rides}")