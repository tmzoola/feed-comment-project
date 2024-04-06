from django.urls import path
from .views import (RegisterView, LoginView, LogoutView, ProfileUpdateView, ProfileView,
                    UsersView, SendFriendRequestView, MyNetworksView, AcceptFriendRequestView, ResetPasswordView,
                    IgnoreFriendRequestView, DeleteFromFriendsView)

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileUpdateView.as_view(), name="profile"),
    path('profile_view/', ProfileView.as_view(), name="profile_view"),
    path('list/', UsersView.as_view(), name="list"),
    path('reset-password/', ResetPasswordView.as_view(), name="reset_password"),



    #users friend request logic
    path('send_request/<int:id>/', SendFriendRequestView.as_view(), name="send_request"),
    path('networks/', MyNetworksView.as_view(), name="my_networks"),
    path('accept-friend/<int:id>/', AcceptFriendRequestView.as_view(), name="accept_friend"),
    path('ignore-friend/<int:id>/', IgnoreFriendRequestView.as_view(), name="ignore_friend"),
    path('delete-friend/<int:id>/', DeleteFromFriendsView.as_view(), name="delete_friend"),
]
