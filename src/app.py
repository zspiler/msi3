from flask import Flask, request, render_template
from pymongo import MongoClient
from flask_caching import Cache

app = Flask(__name__)
db = MongoClient("mongodb://db:27017").test_db
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://redis:6379/0'})

counter = db.col.find_one()
if counter == None:
    db.col.insert_one({ 'counter' : 1 })

@app.route('/', methods=['GET', 'POST'])
@cache.cached(timeout=5)
def main():
    counter = db.col.find_one()['counter'] 
    if request.method == 'POST':
        counter += 1
        db.col.find_one_and_update({}, {'$set': { 'counter': counter }})
    return render_template('index.html', x=counter) 

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
