from flask import Flask
from flask_caching import Cache 
import time
import logging

app = Flask(__name__)
cache=Cache(app,config={'CACHE_TYPE': 'simple'})

logging.basicConfig(level=logging.DEBUG)
Log =  logging.getLogger("Flask Service")

@app.route('/test') 
@cache.cached(timeout=10)
def hello_world(): 
    Log.info("I'm Here I'm gonna sleep !!!!!")
    time.sleep(5)
    Log.info("sleep Done !")
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)