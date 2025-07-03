
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.shortcuts import redirect
from blog import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("blog/", include("blog.urls")),
    # path("", lambda request: redirect("/blog/")),
    path("", views.root)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)