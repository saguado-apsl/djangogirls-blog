from django.shortcuts import render
from blog.models import Post


# Create your views here.

def post_list(request):

    list = Post.objects.all()
    print(list)
    return render(request, 'post_list.html', {'list':list})



