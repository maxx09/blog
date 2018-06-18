from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):

    category = forms.ModelChoiceField(required=True, queryset=Category.objects.all(), to_field_name='category_name')

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'category']