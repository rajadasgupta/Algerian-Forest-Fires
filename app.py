from flask import Flask,request,app,jsonify,url_for,render_template
import sys
from forest.logger import logging
from forest.exception import ForestException
import numpy as np
import pickle

app=Flask(__name__)
model=pickle.load(open('model_rc.pkl','rb'))

@app.route('/',methods=['POST','GET'])
def home():
    try:
        return render_template('home.html')
    except Exception as e:
        forest = ForestException(e,sys)
        logging.info(forest.error_message)

@app.route('/predict',methods=['POST','GET'])
def predict():
    try:
        data=[float(x) for x in request.form.values()]
        final_features = [np.array(data)]
        print(data)
        print(final_features)
    
        output=model.predict(final_features)
        print(output)
        if output == 0:
            chance = "No Chance"
        else:
            chance = "High chances"
        return render_template('home.html', prediction_text="The chances of forest fire is -  {}".format(chance))
    except Exception as e:
        forest = ForestException(e,sys)
        logging.info(forest.error_message)    

if __name__=='__main__':
    app.run(debug=True)


