from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post Title', 'class': 'input-field'}),
            'author': forms.TextInput(attrs={'placeholder': 'Author', 'class': 'input-field'}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your content here...', 'class': 'textarea-field'}),
        }