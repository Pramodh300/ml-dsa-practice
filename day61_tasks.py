from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

#pass or fail
model = pickle.load(open('student_model.pkl','rb'))
@app.route('/predict', methods = ['POST'])

def predict():

    data = request.get_json()
    hours = data['study_hours']
    prediction = model.predict([[hours]])

    return jsonify({
        "Study hours" : hours,
        "Prediction ": "Pass" if prediction == 1 else "Fail"
    })

if __name__ == '__main__':
    app.run(debug = True)


#Titanic survival prediction
model = pickle.load(open('titanic_model.pkl', 'rb'))
columns = pickle.load((open('columns.pkl', 'rb')))

@app.route('/')
def home():
    return "Titanic survival prediction API is running"

@app.route('/predict', methods =['POST'])
def predict():
    data = request.get_json()
    passenger = pd.DataFrame([data])
    passenger = pd.get_dummies(passenger, columns = ['sex', 'embarked'], drop_first = True)
    passenger = passenger.reindex(columns = columns, fill_value=0)

    prediction = model.predict(passenger)
    return jsonify({
        "Passenger": data,
        "Prediction": "Survived" if prediction[0] == 1 else "Did not survive"
    })

if __name__ == '__main__':
    app.run(debug = True)



#House rate prediction
model = pickle.load(open('house_model.pkl', 'rb'))
@app.route('/predict', methods = ['POST'])

def predict():
    data = request.get_json()
    size = data['size']
    bedrooms = data['bedrooms']

    price = model.predict([[size, bedrooms]])

    return jsonify({
        "Size of house " : size,
        "Number of bedrooms " : bedrooms,
        'Price of house' : f"{price[0]:.2f}"
    })

if __name__ == '__main__':
    app.run(debug = True)
