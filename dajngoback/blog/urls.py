from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index),
    path('blogcomment/', views.BlogComment.as_view()),
    path('blogreply/', views.BlogReply.as_view()),
    path('blogcommentview/<int:pk>', views.BlogCommentView.as_view()),
]
