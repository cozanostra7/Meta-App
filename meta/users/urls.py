from django.urls import path
from . import views


urlpatterns = [
    path('',views.profiles,name='profiles'),
    path('user-profile/<str:pk>/',views.getProfile,name='user-profile'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerUser,name='register'),
    path('account/',views.userAccount,name='account'),
    path('edit-account/',views.editAccount,name='edit-account'),
    path('create-skill/',views.createSkills,name='create-skill'),
    path('update-skill/<str:pk>/',views.updateSkills,name='update-skill'),
    path('delete-skill/<str:pk>/',views.deleteSkills,name='delete-skill'),
]