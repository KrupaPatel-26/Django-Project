from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment, Like
from django.contrib.auth.decorators import login_required

# View for blog post list
def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# View for individual blog post with comments
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

# Add a comment
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(post=post, author=request.user, text=text)
    return redirect('post_detail', post_id=post_id)


@login_required
def like_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    user = request.user

    # Check if the user has already liked the post
    if Like.objects.filter(post=post, user=user).exists():
        # Optional: You could remove the like if you want to allow toggling
        Like.objects.filter(post=post, user=user).delete()
    else:
        # Create a new Like entry if it doesn't exist
        Like.objects.create(post=post, user=user)

    return redirect('post_detail', post_id=post.id)
