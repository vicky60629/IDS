import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predict = model.predict(final_features)

    if predict==0:
        output='attacker'
    elif predict==1:
        output='normal'
    elif predict==2:
        output='suspicious'
    elif predict==3:
        output='unknown'
    else:
        output='victim'

    return render_template('index.html', output=output)

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    predict = model.predict([np.array(list(data.values()))])

    if predict==0:
        output='attacker'
    elif predict==1:
        output='normal'
    elif predict==2:
        output='suspicious'
    elif predict==3:
        output='unknown'
    else:
        output='victim'

    return jsonify(output)

if __name__ == "__main__":
    app.run()
