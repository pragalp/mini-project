import requests
from django.shortcuts import render

NEWS_API_KEY = '1a19dba919de4c928d46dcfc57702342'

def news_page(request):
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return render(request, 'news.html', {'articles': articles})

def jokes_page(request):
    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    joke_data = response.json()

    if joke_data['type'] == 'single':
        joke = joke_data['joke']
    else:
        joke = f"{joke_data['setup']} ... {joke_data['delivery']}"

    return render(request, 'jokes.html', {'joke': joke})
