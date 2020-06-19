from django.shortcuts import render
from .models import Title
# Create your views here.


def index(request):
    return render(request, 'blogs/index.html')


def titles(request):
    titles = Title.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/titles.html', context)


def title(request, title_id):
    title = Title.objects.get(id=title_id)
    descriptions = title.description_set.order_by('-date_added')
    context = {'title': title, 'descriptions': descriptions}
    return render(request, 'blogs/title.html', context)
