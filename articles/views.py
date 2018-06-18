from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm

def index(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, "index.html",{
        'post_list':post_list,
        'category_list':category_list
    })


def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else:
        form = PostForm()
    return render(request, 'articles/post_create.html', {'form':form})



def get_post_detail(request, post_id):

    pass