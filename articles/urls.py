from django.conf.urls import url
from .views import index, create_post

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^post/$', create_post, name='post'),
]