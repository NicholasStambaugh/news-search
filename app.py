from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='f39095ae8be4476db173a4fafae9fe53')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
        return render_template('results.html', articles=articles['articles'])

    return render_template('index.html')

@app.route('/results', methods=['GET'])
def results():
    query = request.args.get('q')
    api_key = newsapi
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    response = requests.get(url)
    articles = response.json()['articles']
    return render_template('results.html', articles=articles)


if __name__ == '__main__':
    app.run(debug=True)

