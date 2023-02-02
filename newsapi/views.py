from django.shortcuts import render, HttpResponse
import requests
API_KEY = '5461a49000b846018c631e13881934b8'

# Create your views here.

def home(request):
    country = request.GET.get('country')
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    context = {
        'articles':articles
    }

    return render(request, 'newsapi/home.html', context)
