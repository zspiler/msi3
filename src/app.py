from flask import Flask, request, render_template, abort
from pymongo import MongoClient
from flask_caching import Cache
import socket

app = Flask(__name__)
db = MongoClient("mongodb://mongo-svc.default.svc.cluster.local:27017").test_db

cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://redis-svc.default.svc.cluster.local:6379/0'})
hostname = socket.gethostname()

counter = db.col.find_one()
if counter == None:
    db.col.insert_one({ 'counter' : 1 })

@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def main():
    counter = db.col.find_one()['counter'] 
    counter += 1
    db.col.find_one_and_update({}, {'$set': { 'counter': counter }})        
    return render_template('index.html', x=counter, host=hostname) 

@app.route('/readiness-check', methods=['GET', 'POST'])
def readiness():
    try:
        MongoClient("mongodb://mongo-svc.default.svc.cluster.local:27017").server_info() 
        return f"ready, db: {db}"
    except:
        abort(500)

@app.route('/liveness-check', methods=['GET', 'POST'])
def liveness():
        return "I am very much alive"

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
