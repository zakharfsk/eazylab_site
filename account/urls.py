from django.urls import path

from . import views

urlpatterns = [
    path('account/', views.account_page, name='account'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]
