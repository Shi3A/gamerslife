from django.conf.urls import url

from post import views

urlpatterns = [
    url(r'^create$', views.PostCreateView.as_view(), name="create-post"),
]
