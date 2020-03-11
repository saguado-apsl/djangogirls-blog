from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from blog.models import Post
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.


def post_list(request):

    my_list = Post.objects.all()
    print(my_list)
    return render(request, 'post_list.html', {'list': my_list})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=int(pk))
    return render(request, 'post_detail.html', {'post': post})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 
            post.autor = request.user
            post.published_date = timezone.now()
            post.save()
            type(post.pk)
            passInteger = int(post.pk)
            return redirect('post', pk=passInteger)

    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})


def edit_post():

    return render(request, 'edit.html')