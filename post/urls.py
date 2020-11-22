from django.urls import path, include

import gamepage
from post import views

app_name = 'post'

urlpatterns = [
    path('add/', views.PostCreateView.as_view(), name='add-post'),
    path('allpost/', views.post_list, name='all-post'),
    path('allpost/<int:pk>/', views.post_detail, name='detail'),
    path('allpost/<int:pk>/', views.post_favourite, name='favourite'),
    path('allpost/<tag_slug>/', views.post_by_tag, name='tagged_post'),
]
