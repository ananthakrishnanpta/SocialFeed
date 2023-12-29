from django.urls import path 
# from . import views
from .views import FeedView, MessageDetailView, CreateMessageView, EditMessageView, DeleteMessageView, LikeView

urlpatterns = [
    #path('', views.home, name="home"),
    path('', FeedView.as_view(), name='feed'),
    path('message/<int:pk>', MessageDetailView.as_view(), name='message-detail'),
    path('add_msg/', CreateMessageView.as_view(), name='add-msg'),
    path('message/edit/<int:pk>', EditMessageView.as_view(), name='edit-msg'),
    path('message/del/<int:pk>', DeleteMessageView.as_view(), name='del-msg'),
    path('like/<int:pk>', LikeView, name='like-msg')
]

