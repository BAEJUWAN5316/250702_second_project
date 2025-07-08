from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/<int:pk>/", views.post_detail),  
    path("<str:username>/<int:pk>/post/edit/", views.post_edit),
    path("<str:username>/<int:pk>/post/delete/", views.post_delete),
    path("<str:username>/write/", views.post_form),
    path("<str:username>/", views.post_list, name="post_list"),
    path("user/<int:post_pk>/comment/", views.comment_form),
    path("user/<int:comment_pk>/comment/edit/", views.comment_edit),
    path("user/<int:post_pk>/comment/<int:comment_pk>/delete/", views.comment_delete),
]