from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# ✅ Load the trained pipeline
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Extract form inputs
        name = request.form['name']
        year = int(request.form['year'])
        km_driven = int(request.form['km_driven'])
        fuel = request.form['fuel']
        seller_type = request.form['seller_type']
        transmission = request.form['transmission']
        owner = request.form['owner']

        # ✅ Create a DataFrame with the correct column names
        input_df = pd.DataFrame([{
            'name': name,
            'year': year,
            'km_driven': km_driven,
            'fuel': fuel,
            'seller_type': seller_type,
            'transmission': transmission,
            'owner': owner
        }])

        # ✅ Predict using the pipeline
        prediction = model.predict(input_df)[0]

        return render_template('index.html', prediction=round(prediction, 2))

    except Exception as e:
        return f"Prediction Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
