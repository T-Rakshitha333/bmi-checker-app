from flask import Flask, render_template, request
from math import pow

app = Flask(__name__, template_folder='.')  # This tells Flask to look in the root directory for templates

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_bmi():
    try:
        height = float(request.form['height']) / 100  # Convert to meters
        weight = float(request.form['weight'])
        bmi = round(weight / pow(height, 2), 1)

        if bmi < 18.5:
            result = f'BMI = {bmi} is Underweight'
        elif 18.5 <= bmi < 24.9:
            result = f'BMI = {bmi} is Normal'
        elif 24.9 <= bmi < 29.9:
            result = f'BMI = {bmi} is Overweight'
        else:
            result = f'BMI = {bmi} is Obesity'

        return render_template('index.html', result=result)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
