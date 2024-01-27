from flask import Flask
from flask_caching import Cache
import random
import requests
from flask import request

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379/0'})

@app.route("/route1")
@cache.cached(timeout=20)
def route1():
    url = "https://www.abibliadigital.com.br/api/verses/nvi/sl/23Search"
    response = requests.get(url)
    return response.json()


@app.route("/search")
@cache.cached(timeout=50,query_string=True) #flask cache defaultly takes path variable for keys 
#use this query string to make the names based the query string
def search():
    query = request.args.get('query','').replace(' ','+')
    url = 'https://openlibrary.org/search.json?q={}'.format(query)
    print(url)
    response = requests.get(url)
    return response.json()
    
    data = str(random.randint(0,100000))  + '\n'
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
