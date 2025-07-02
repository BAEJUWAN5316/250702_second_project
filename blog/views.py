from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Post, Comment
from blog.forms import PostForm

# Create your views here.

# 메인페이지
def blog_main():
    pass


# 포스트 목록 페이지
def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/post_list.html")


# 포스트, 댓글 페이지
def post_detail(request: HttpRequest, pk) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    title = post.title
    description = post.description
    photo = post.photo
    music = post.music

    return render(
        request,
        "blog/post_detail.html",
        context={"title": title, "description":description, "photo":photo, "music":music}
        )


# 포스트 쓰기 페이지
def post_form(request: HttpRequest, pk:int) -> HttpResponse:
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_post: Post = form.save(commit=False)
            unsaved_post.save()
            post_url = f"blog/user/{pk}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/post_form.html",
        {"form":form}
    )

# 댓글쓰기
def comment_form():
    pass


# 회원가입 페이지 > accounts 앱에서 만들기


# 로그인 페이지  > accounts 앱에서 만들기