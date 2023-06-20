from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as coreview

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('', coreview.home, name="home"),
    path('signup/', coreview.signup, name="signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('profiles/', coreview.profiles, name="profiles"),
    path('change_staff_status/', coreview.change_staff_status, name='change_staff_status'),
]

