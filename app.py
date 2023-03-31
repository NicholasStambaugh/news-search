# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        api_key = 'f39095ae8be4476db173a4fafae9fe53'
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
        response = requests.get(url)
        articles = response.json()['articles']
        return render_template('index.html', articles=articles, query=query)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
