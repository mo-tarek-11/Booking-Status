import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def homee():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    Lead_Time= request.form.get('Lead_Time')
    Market_Segment_Type = request.form.get('Market_Segment_Type')
    AVG_Price= request.form.get('AVG_Price')
    Special_Requests = request.form.get('Special_Requests')
    Date_of_Reservation = request.form.get('Date_of_Reservation')
    year = request.form.get('year')
    float_features  = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction == 1:
        output ='Not Canceled'
    else:
        output ='Canceled'
    
    return render_template('Res.html',prediction_text="{}".format(output)
                           ,Lead_Time=Lead_Time
                           ,Market_Segment_Type=Market_Segment_Type
                           ,AVG_Price=AVG_Price
                           ,Special_Requests=Special_Requests
                           ,Date_of_Reservation=Date_of_Reservation
                           ,year=year)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005)