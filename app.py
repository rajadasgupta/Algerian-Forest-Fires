from flask import Flask
import sys
from forest.logger import logging
from forest.exception import ForestException

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    try:
        raise Exception("we are testing custom expection")
    except Exception as e:
        forest = ForestException(e,sys)
        logging.info(forest.error_message)    
        logging.info("We are testing the logging module")
    return " Testing exception in Forest project. Added CI/CD pipleine as well"

if __name__=='__main__':
    app.run(debug=True)


