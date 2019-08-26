from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name='Blog_home'),
    url(r'^new/$', views.PostCreateView.as_view(), name='Blog_create'),
]