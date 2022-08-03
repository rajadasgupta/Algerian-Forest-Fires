from flask import Flask
import sys
from forest.logger import logging
from forest.exception import ForestException

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    try:
        raise ForestException("we are testing custom expection")
    except Exception as e:
        forest = ForestException(e,sys)
        logging.info(forest.error_message)    
        logging.info("We are testing the logging module")
    return " Testing exception in Forest project. Added exception handling and logging"

if __name__=='__main__':
    app.run(debug=True)


