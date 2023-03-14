from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Category, Tag
from .forms import PostForm, UpdatePostForm, CommentForm, UserProfileForm, UserForm, CategoryForm

# Create your views here.

# def blog_page(request):

#     return render(request, 'blog/blog.html')


def blog_page(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.filter(Q(title__icontains=q) |
    Q(category__name__icontains=q) |
    Q(body__icontains=q)
    # Q(author__name__icontains=q)  
    )
    post_count = posts.count()
    # post_comment = Comment.objects.filter(Q(post__category__name__icontains=q) |
    # Q(post__name__icontains=q)
    # )


    # context = {'rooms':rooms, 'topics':topics, 'room_count':room_count, 'room_message':room_message}
    # return render(request, 'base/home.html', context)

    context = {'posts':posts, 'categories':categories, 'post_count':post_count, 'tags':tags}
    return render(request, 'blog/blog.html', context)

def login_user(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return HttpResponse('User is not active!')
        else:
            return HttpResponse('Invalid Password or Username!')
    else:
        context = {}
        return render(request, 'registration/login.html', context)

        
def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    registered = False
    user_form = UserForm()
    profile_form = UserProfileForm()

    if request.method == 'POST':

        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True


        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    context = {'registered':registered, 'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'registration/register.html', context)


def post_page(request, pk):
    post = Post.objects.get(id=pk)
    # post_messages = post.message_set.all()
    # participants = room.participants.all()

    if request.method == 'POST':
    #     comment = Comment.objects.create(
    #         user = request.user,
    #         post = post,
    #         body = request.POST.get('body')
    #     )
        # room.participants.add(request.user)
        return redirect('post', pk=post.id)

    # context = {'room':room, 'post_messages':post_messages, 'participants':participants}
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)

# def user_profile(request, pk):
#     user = User.objects.get(id=pk)
#     post_messages = user.message_set.all()
#     posts = user.post_set.all()
#     categories = Category.objects.all()
#     context = {'user':user, 'posta':posts, 'post_messages':post_messages, 'categories':categories}
#     return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)

# @login_required(login_url='login')
def add_category(request):
    form = CategoryForm()
    categories = Category.objects.all()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form':form, 'categories':categories}
    return render(request, 'blog/categories.html', context)

def post_category(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    context = {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts}
    return render(request, 'blog/add_category.html', context)

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post-list')

@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = UpdatePostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(post_page, pk=post.pk)
    context = {'form':form}
    return render(request, 'blog/update_post_form.html', context)

@login_required(login_url='login')
def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    context = {'obj':post}
    return render(request, 'post/delete.html', context)

def add_comment_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {'form':form}
    return render(request, 'blog/comment_form.html', context)


@login_required(login_url='login')
def comment_approve(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment_pk = comment.post.pk
        comment.approve()
        return redirect('post-detail', pk=comment_pk)
    context = {'object':comment}
    return render(request, 'blog/approve_form.html', context)


@login_required(login_url='login')
def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk)

    if request.method == 'POST':
        comment_pk = comment.post.pk
        comment.delete()
        return redirect('post-detail', pk=comment_pk)
    context = {'object':comment}
    return render(request, 'blog/delete.html', context)

@login_required(login_url='login')
def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment_pk = comment.post.id
            return redirect('post-detail')

def searched(request):

    context = {}
    return render(request, 'blog/searched.html', context)
