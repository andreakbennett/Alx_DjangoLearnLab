from django.urls import path
from .views import RegisterView, ProfileView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', obtain_auth_token, name='login') ,
]


from django.urls import path
from .views import FollowViewSet

follow_view = FollowViewSet.as_view({
    'post': 'follow'
})

unfollow_view = FollowViewSet.as_view({
    'post': 'unfollow'
})

urlpatterns = [
    path('follow/<int:pk>/', follow_view, name='follow'),
    path('unfollow/<int:pk>/', unfollow_view, name='unfollow'),
]
