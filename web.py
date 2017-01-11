from flask import *
import pandas as pd
from scripts import test as test,youtube as y
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('search.html')

@app.route('/opt')
def hello_world():
	data=test.getTwitterTrends()
        return render_template('trends.html',data=data)

@app.route('/search',methods=['GET','POST'])
def indexing():
	error = None
	if request.method == "POST":
            query = request.form['q']
            data= test.worker(query)
            #print data
            youtube=y.getVideos(query,40)
            #d1=youtube.sort(['viewCount'], ascending=True, inplace=True)
            subset = youtube[['title','viewCount','publishedTime']]
            tuples = [tuple(x) for x in subset.values]
            return render_template('search.html',q=data,yTitle=tuples)

if __name__ == '__main__':
	app.run(debug=True)
