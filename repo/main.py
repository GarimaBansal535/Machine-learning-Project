import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        temperature = request.form.get('temperature')
        if temperature is None or temperature.strip() == "":
            raise ValueError("No temperature provided")
        
        temperature = float(temperature)
        prediction = model.predict([[temperature]])
        output = round(prediction[0], 2)
        print(output)
        return render_template('index.html', prediction_text=f'Total Revenue generated is Rs.: {output}/-')
    except ValueError as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')


if __name__ == '__main__':
    app.run(debug=True)