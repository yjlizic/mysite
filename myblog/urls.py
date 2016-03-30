from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'myblog.views.blog_index', name='blog_index'),
]