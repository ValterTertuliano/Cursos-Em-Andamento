from django.urls import path
from blogapp import views

app_name = 'blogapp' 

urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<int:id>/", views.post_view, name="post"),
    path("exemplo/", views.exemploblog, name="exemplo"),
]
