from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='enter_your_api_key_here')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        sort_by = request.form['sort_by']
        articles = newsapi.get_everything(q=query, language='en', sort_by=sort_by)
        return render_template('results.html', articles=articles['articles'])
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


