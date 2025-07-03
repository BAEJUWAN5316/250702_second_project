from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/", views.post_list), # 포스팅 리스트(개인 블로그)
    # path("user/list/", views.post_list), #포스팅 리스트
    path("<str:username>/<int:pk>/", views.post_detail), #포스팅 내용
    path("<str:username>/write/", views.post_form), # 포스트 작성
    path("<str:username>/<int:pk>/post/edit/", views.post_edit), # 포스트 수정
    path("user/<int:pk>/post/delete/", views.post_delete), # 포스트 삭제
    path("user/<int:post_pk>/comment/", views.comment_form), # 댓글 작성
    path("user/<int:comment_pk>/comment/edit/", views.comment_edit), # 댓글 수정
    path("user/<int:post_pk>/comment/<int:comment_pk>/delete/", views.comment_delete), # 댓글삭제
]