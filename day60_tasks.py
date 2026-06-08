from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

#Home
@app.route('/')
def home():
    return "Welcome! Go to /users to see the JSON data."

#Users
@app.route('/users')
def users():
    return jsonify(
        {
            "name":"Pramodh",
            "role":"AI Engineer"
        }
    )

#About
@app.route('/about')
def about():
    return 'About page'


#Student
@app.route('/student')
def student():
    return jsonify({
        "name" : "ABC",
        "Course" : "CSE",
        "college" : "College of college"
    })

#pass or fail
model = pickle.load(open('student_model.pkl','rb'))
@app.route('/predict', methods = ['POST'])

def predict():

    data = request.get_json()
    hours = data['study_hours']
    prediction = model.predict([[hours]])

    return jsonify({
        "Prediction ": int(prediction[0])
    })

if __name__ == '__main__':
    app.run(debug = True)