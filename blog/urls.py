from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list), #메인화면
    path("user/list/", views.post_list), #포스팅 리스트
    path("user/<int:pk>/", views.post_detail), #포스팅 내용
    path("user/postform/<int:pk>", views.post_form), # 포스트 작성
    path("user/<int:pk>/comments/", views.comment_form), # 댓글 작성
]