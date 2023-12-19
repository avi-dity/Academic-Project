from flask import *
import pickle
import pandas as pd

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('Logistic_Regression.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/predict", methods = ['POST'])
def predict():
      if request.method == 'POST':
                review = str(request.form['fn'])
                pred = model.predict(pd.DataFrame({'reviewText':[review]}))
                return render_template('index.html',results=pred[0])
      else:
             return render_template('index.html')


if __name__ == "__main__":
	app.run(debug = True)
