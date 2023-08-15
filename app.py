import numpy as np
import pickle
# Flask utils
from flask import Flask, redirect, url_for, request, render_template

# Define a flask app
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

print('Model loaded. Start serving...')

print('Check http://127.0.0.1:5000/')


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def get_data():
    print("inside post")
    if request.method == 'POST':
        # Get the file from post request
        age = request.form['age']
        print(type(age))
        gender = request.form['gender']
        Polyuria = request.form['Polyuria']
        Polydipsia = request.form['Polydipsia']
        Weight = request.form['Weight']
        Weakness = request.form['Weakness']
        Polyphagia = request.form['Polyphagia']
        Thrush = request.form['Thrush']
        Blurring = request.form['Blurring']
        Itching = request.form['Itching']
        Irritability = request.form['Irritability']
        Healing = request.form['Healing']
        Paresis = request.form['Paresis']
        Stiffness = request.form['Stiffness']
        Alopecia = request.form['Alopecia']
        Obesity = request.form['Obesity']
        newpat = [[age,gender,Polyuria,Polydipsia,Weight,Weakness,Polyphagia,Thrush,Blurring,Itching,Irritability,Healing,Paresis,Stiffness,Alopecia,Obesity]]
        print(type(newpat))
        result = clf.predict(newpat)
        print(result)
        if result == 1:
            val = "Diabetes"
        else:
            val = "No Diabetes"
            
            
    return render_template('/templates/index.html',value=val)


if __name__ == '__main__':
    app.run(debug=True)
