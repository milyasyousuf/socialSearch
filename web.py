from flask import *
import pandas as pd
from scripts import twitterTrends as tT
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opt')
def hello_world():
	i=0
 	if i==0:
		d1 = pd.DataFrame()
		df = tT.testing(10)
		d1['location'] = df['location']
		d1['trendname'] = df['trendname']
		d1['tweet_volume'] = df['tweet_volume']
		d1['trendStart'] = df['trendStart']
		d1 = d1.groupby(d1['trendname']).head(10)
		d1 = d1.to_html(classes="table table-hover", index=False)
		d1 = d1.replace('border="1"', '')
		    # dfH = dfH.replace('link', "<a href='http://example.com/'>Click</a>")
		d1 = d1.replace('link', "<a href='#''>Click</a>")
		i=i+1
	
	return render_template('index.html', totalAccts=100, totalBal=100, list=d1)


def search()

if __name__ == '__main__':
    app.run(debug=True)
