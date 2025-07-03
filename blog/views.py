from django.http import HttpRequest, HttpResponse, Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from blog.forms import PostForm, CommentForm

# Create your views here.

# 메인페이지
def blog_main():
    pass


# 포스트 목록 페이지
def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(
        request, 
        "blog/post_list.html",
        context={"post_list": qs}
        )


# 포스트, 댓글 페이지
def post_detail(request: HttpRequest, pk) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    title = post.title
    description = post.description
    photo = post.photo
    music = post.music
    comment_qs = Comment.objects.all()
    comment_qs = comment_qs.filter(post=post)

    return render(
        request,
        "blog/post_detail.html",
        context={"title": title, "description":description, "photo":photo, "music":music, "post":post, "comment_list": comment_qs}
        )


# 포스트 쓰기 페이지
def post_form(request:HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_post: Post = form.save(commit=False)
            unsaved_post.save()
            post_url = f"/blog/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/post_form.html",
        {"form":form}
    )
# 포스트 수정 페이지
def post_edit(request:HttpRequest, pk:int):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            post_url = f"/blog/user/{pk}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/post_form.html",
        {"form":form, "post":post}
    )

# 포스트 지우기
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "GET":
        return render(request, "blog/post_confirm_delete.html")
    
    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return redirect("/blog/")


# 댓글쓰기
def comment_form(request:HttpRequest, post_pk:int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "GET":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_comment: Comment = form.save(commit=False)
            unsaved_comment.post = Post.objects.get(id=post_pk)
            unsaved_comment.save()
            post_url = f"/blog/user/{post_pk}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/comment_form.html",
        {"form":form}
    )

def root(request):
    return render(request, "root.html")

# 댓글 지우기

# 회원가입 페이지 > accounts 앱에서 만들기


# 로그인 페이지  > accounts 앱에서 만들기