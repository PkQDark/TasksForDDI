# -*- coding: utf-8 -*-
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/blog/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cur_user = authenticate(username=username, password=password)
        if cur_user is not None:
            login(request, cur_user)
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Неверный логин/пароль.')

    return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        general = UserCreationForm(request.POST)
        if general.is_valid():
            username = general.cleaned_data['username']
            try:
                User.objects.get(username=username)
                messages.add_message(request, messages.ERROR,
                                     'Пользователь с таким ником ' + username + ' уже зарегистрирован')
            except User.DoesNotExist:
                user = general.save()
                user.save()
                messages.add_message(request, messages.SUCCESS,
                                     'Пользователь успешно зарегистрирован')
                return HttpResponseRedirect('/blog/')
    else:
        general = UserCreationForm()
    return render(request, 'blog/register.html',
                  {'general': general})


@login_required
def home(request):
    cur_user = request.user.username
    blogs = Post.objects.all()
    return render(request, 'blog/home.html', {'blogs': blogs, 'cur_user': cur_user})


@login_required
def add_post(request):
    cur_user = request.user.username
    user = User.objects.get(username=cur_user)
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            try:
                Post.objects.get(title=post_form.cleaned_data['title'])
                messages.add_message(request, messages.WARNING, 'Пост с таким названием уже существует, придумайте новое')
            except Post.DoesNotExist:
                cur_post = Post(author=user,
                                title=post_form.cleaned_data['title'],
                                content=post_form.cleaned_data['content'])
                cur_post.save()
                messages.add_message(request, messages.SUCCESS, 'Блог успешно добавлен')
            return HttpResponseRedirect('/blog/')
    else:
        post_form = PostForm()
    return render(request, 'blog/add_post.html', {'post': post_form, 'cur_user': cur_user})


def pagination(list_of_comments, per_page):
    try:
        per_page = int(per_page)
    except (TypeError, ValueError):
        raise Exception('Wrong num')
    num_of_pages = int(len(list_of_comments)/per_page) + 1
    answer_list = []
    for i in range(num_of_pages):
        answer_list.append(list_of_comments[i*per_page:(i+1)*per_page])
    return answer_list, num_of_pages


@login_required
def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = User.objects.get(username=request.user.username)
    comments = post.comment_set.filter(post_id=post)
    pagination_list, pages = pagination(comments, 5)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                post_id=post,
                author_id=user,
                content=comment_form.cleaned_data['comment'],
            )
            comment.save()
            path = None
            if request.POST.get('parent_path'):
                path = request.POST.get('parent_path')
            cur_path = ''
            if path:
                cur_path += path + ' ' + str(comment.id)
            else:
                cur_path = str(comment.id)
            comment.path = cur_path

            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Коментарий успешно добавлен')
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()

    page = 0

    if request.GET.get('page'):
        page = int(request.GET.get('page')) - 1

    next_page = page + 1
    previous_page = page - 1
    return render(request, 'blog/post.html', {
        'post': post,
        'pagination_list': pagination_list[page],
        'cur_page': page + 1,
        'next_page': None if next_page >= pages else next_page + 1,
        'previous_page': None if previous_page < 0 else previous_page + 1,
        'cur_user': request.user.username,
        'comment_form': comment_form,
        'pages': pages
    })