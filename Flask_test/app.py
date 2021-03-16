from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle 
import numpy as np

app = Flask(__name__)
# load the pickle file
model = pickle.load(open('Flask_test\model.pkl', 'rb'))
# create dictionaries
day_dict = {'Fri':[1,0,0,0,0,0,0], 'Mon':[0,1,0,0,0,0,0],
            'Sat': [0,0,1,0,0,0,0], 'Sun':[0,0,0,1,0,0,0],
            'Thu':[0,0,0,0,1,0,0], 'Tue':[0,0,0,0,0,1,0],
            'Wed': [0,0,0,0,0,0,1]}

mon_dict = {"January":[0,0,0,0,1,0,0,0,0,0,0,0], 'February':[0,0,0,1,0,0,0,0,0,0,0,0],
            'March': [0,0,0,0,0,0,0,1,0,0,0,0], 'April':[1,0,0,0,0,0,0,0,0,0,0,0],
            'May':[0,0,0,0,0,0,0,0,1,0,0,0], 'June':[0,0,0,0,0,0,0,1,0,0,0,0],
            'July': [0,0,0,0,0,0,1,0,0,0,0,0], "August":[0,1,0,0,0,0,0,0,0,0,0,0],
            "September":[0,0,0,0,0,0,0,0,0,0,0,1],"October":[0,0,0,0,0,0,0,0,0,0,1,0],
            "November":[0,0,0,0,0,0,0,0,0,1,0,0], "December":[0,0,1,0,0,0,0,0,0,0,0,0]}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    item = [x for x in request.form.values()]
    print(item)

    data = []

    data.append(int(item[0]))

    # As the The training data was dummified, I have to pass the test data in the same format ('hour','is_holiday','day_of_week')
       
    # is holiday
    if item[3] == 'Yes':
        data.extend([0,1])
    else:
        data.extend([1,0])

    # member vs casual
    if item[4] == 'Yes':
        data.extend([1,0])
    else:
        data.extend([0,1])
        
    # fri, mon, sat , sun, thu, tue, wed
    data.extend(mon_dict[item[1]])

    # month

    data.extend(day_dict[item[2]])
   
    prediction = int(model.predict([data])[0])
    
    # postman begin

    # return 'the predicted total bike count :' + str(prediction) 

    # postman end

    return render_template('index.html',pred='Total Bike ride counts on {} during the month of {} at {}:00 Hrs by {} members will be {}'.format(item[1],item[2],item[0],item[4],prediction))

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)


if __name__ == "__main__":
    app.run(debug=True)
