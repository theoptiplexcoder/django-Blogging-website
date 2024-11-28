from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import BlogPost

app_name='blogs'

class HomeView(generic.ListView):
    template_name="blogSpace/home.html"
    context_object_name="blogList"
    def get_queryset(self):
        return BlogPost.objects.all()
    
class DetailView(generic.DetailView):
    model=BlogPost
    template_name="blogSpace/detail.html"

def createPost(request):
    if request.method=='POST':
        content=request['POST']
    return render(request,"blogSpace/create.html")