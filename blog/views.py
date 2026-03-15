from django.shortcuts import render, get_object_or_404,redirect
from .models import Post
from datetime import datetime
from .forms import ContactForm

def home(request):
    blogs = Post.objects.all()
    return render(request, "blog/home.html", {
        "blogs": blogs,
        "year": datetime.now().year
    })

def base(request):
    return render(request,"blog/base.html")

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "blog/post_detail.html", {"post": post})

def about(request):
    return render(request,"blog/about.html")

def blog(request):
    return render(request,"blog/blog.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ye automatically data db me save karega
            return redirect('contact')  # ya thank you page
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})