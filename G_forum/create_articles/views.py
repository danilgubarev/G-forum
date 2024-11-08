from django.shortcuts import render

from create_articles.models import *
# Create your views here.

def add_articles_view(request):

    if request.method == 'POST':
        heading = request.POST.get('heading')
        text = request.POST.get('text')
        print(heading)
        print(text)
        SaveArticles.objects.create(heading = heading, text = text)
        
    return render(request, 'create_articles/create_articles.html')