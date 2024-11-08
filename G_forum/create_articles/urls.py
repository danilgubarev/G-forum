from django.urls import path 

from create_articles.views import *

app_name = 'create_articles'

urlpatterns = [
    path('create/', add_articles_view, name = 'add_articles_view')
]