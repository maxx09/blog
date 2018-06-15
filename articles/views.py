from django.shortcuts import render
from .models import Post, Category

def index(request):
    web_list = Post.objects.filter(category__category_name='Web')
    mobile_list = Post.objects.filter(category__category_name='Mobile')
    iot_list = Post.objects.filter(category__category_name='IoT')
    life_list = Post.objects.filter(category__category_name='Life')
    post_list = Post.objects.all()
    return render(request, 'index.html', 
        {'web_list':web_list,
        'mobile_list':mobile_list,
        'iot_list':iot_list,
        'life_list':life_list,
        'post_list':post_list})


def index1(request):
    category_list = Category.objects.all()
    for category in category_list:
        posts = Post.objects.filter(category__category_name=category)
    
    print(posts)

    return render(request, 'base.html',{
        'category_list':category_list,
        'post_list':post_list
    })