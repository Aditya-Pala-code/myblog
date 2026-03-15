from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from blog.models import Post

# 1. Dashboard - List all posts
def dashboard(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'posts': posts})

# 2. Add Post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'dashboard/add_post.html', {'form': form})

# 3. Update Post
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)
    return render(request, 'dashboard/update_post.html', {'form': form, 'post': post})

# 4. Delete Post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')
    return render(request, 'dashboard/delete_post.html', {'post': post})

# 5. View Post - Full description
def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'dashboard/view_post.html', {'post': post})