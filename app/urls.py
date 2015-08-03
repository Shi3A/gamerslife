from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^post/', include('post.urls', namespace='post', app_name='post')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'base.views.index'),
]
