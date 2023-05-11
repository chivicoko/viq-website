from django.urls import path
from .views import IndexView, PostDetailView, CreatePostView, UpdatePostView, PostDelete, CustomLoginView, RegisterPage
# Logout Authentication.
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # login/logout urls
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    # blog urls
    path('', IndexView.as_view(), name='home'),
    path('article/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('article/new/', CreatePostView.as_view(), name='post-new'),
    path('article/<int:pk>/update', UpdatePostView.as_view(), name='post-update'),
    path('article/<int:pk>/delete', PostDelete.as_view(), name='post-delete'),

]