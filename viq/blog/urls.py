from django.urls import path
# from . import views

from .views import IndexView, PostDetailView, CreatePostView, UpdatePostView, PostDelete

urlpatterns = [
    # for function-based view
    # path('', views.indexView, name='home'),

    # for class-based view
    path('', IndexView.as_view(), name='home'),
    path('article/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('article/new/', CreatePostView.as_view(), name='post-new'),
    path('article/<int:pk>/update', UpdatePostView.as_view(), name='post-update'),
    # path('article/<int:pk>/delete', deletePost, name='post-delete'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='post-delete'),

]