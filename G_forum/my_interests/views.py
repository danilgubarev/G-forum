from django.shortcuts import render

# Create your views here.



def my_interests_view(request):
    return render(request, 'my_interests/my_interests.html')