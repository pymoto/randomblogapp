from django.shortcuts import render, redirect
from .random_blog import random_url_get
import random, webbrowser

# Create your views here.

def randombtnfunc(request):
    topiclist = []
    article_list = []
    random_url_get('https://hatenablog.com/topics/journal', '.topic-list-item', topiclist)
    random_url_get(random.choice(topiclist), '.entry-link', article_list)
    randomurl = random.choice(article_list)
    print(randomurl)
    return render(request, 'randombtn.html', {'randomurl':randomurl})