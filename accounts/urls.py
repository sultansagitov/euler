from django.urls import path, include
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from . import views
from . import api_views


urlpatterns = [
    path('', lambda request: redirect(reverse("profile"))),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.editprofile, name='editprofile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.register, name='signup'),

    path('friends/', views.friends, name="friends"),
    path('sendrequest/<str:touser>/', api_views.sendrequest, name="sendrequest"),
    path('acceptrequest/<int:friendrequest>/', api_views.acceptrequest, name="acceptrequest"),
    path('declinerequest/<int:friendrequest>/', api_views.declinerequest, name="declinerequest"),
    path('unfriend/<str:exfriend>/', api_views.unfriend, name="unfriend"),

    path('upload_avatar', api_views.upload_avatar, name="upload_avatar"),
    path('change_theme', api_views.change_theme, name="change_theme"),
    
]
