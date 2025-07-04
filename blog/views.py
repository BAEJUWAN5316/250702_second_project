from django.http import HttpRequest, HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

# 메인페이지
def blog_main():
    pass


# 포스트 목록 페이지
def post_list(request: HttpRequest, username) -> HttpResponse:
    blog_owner = get_object_or_404(User, username=username)

    query = request.GET.get("q", "")
    if query:
        posts = Post.objects.filter(
            author=blog_owner
        ).filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        posts = Post.objects.filter(author=blog_owner)

    is_owner = request.user == blog_owner

    return render(
        request, 
        "blog/post_list.html",
        context={"post_list": posts, "blog_owner":blog_owner, "is_owner":is_owner, "query":query}
        )


# 포스트, 댓글 페이지
def post_detail(request: HttpRequest, username:str, pk:int) -> HttpResponse:
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
        context={"title": title, "description":description, "photo":photo, "music":music, "post":post, "comment_list": comment_qs, "username":username}
        )


# 포스트 쓰기 페이지
def post_form(request:HttpRequest, username: str) -> HttpResponse:
    if request.user.username != username:
        return HttpResponseForbidden("안됩니다.")

    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            unsaved_post: Post = form.save(commit=False)
            unsaved_post.author = request.user
            unsaved_post.save()
            post_url = f"/blog/{username}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/post_form.html",
        {"form":form}
    )
# 포스트 수정 페이지
def post_edit(request:HttpRequest, pk:int, username:str):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            post_url = f"/blog/{username}/{pk}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/post_form.html",
        {"form":form, "post":post}
    )

# 포스트 지우기
def post_delete(request: HttpRequest, pk: int, username:str) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return render(
            request, 
            "blog/confirm_delete.html", 
            {"username":username, "post":post})
    
    post.delete()

    delete_url = f"/blog/{username}/"
    return redirect(delete_url)


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
            unsaved_comment.author = request.user
            unsaved_comment.save()

            username = post.author.username
            post_url = f"/blog/{username}/{post_pk}/"
            return redirect(post_url)
        
    return render(
        request,
        "blog/comment_form.html",
        {"form":form}
    )

# 댓글 수정하기
def comment_edit(request:HttpRequest, comment_pk:int):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == "GET":
        form = CommentForm(instance=comment)
    else:
        form = CommentForm(instance=comment, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            post_pk = comment.post.pk
            comment_url = f"/blog/user/{post_pk}/"
            return redirect(comment_url)
        
    return render(
        request,
        "blog/comment_form.html",
        {"form":form, "comment":comment}
    )

# 댓글 지우기
def comment_delete(request: HttpRequest,post_pk:int, comment_pk: int) -> HttpResponse:
    if request.method == "GET":
        return render(request, "blog/confirm_delete.html")
    
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()

    post_url = f"/blog/user/{post_pk}/"
    return redirect(post_url)


# 메인화면
def root(request):
    user_list = User.objects.all()
    return render(
        request, 
        "root.html",
        {"user_list":user_list}
        )

# 회원가입 페이지 > accounts 앱에서 만들기


# 로그인 페이지  > accounts 앱에서 만들기