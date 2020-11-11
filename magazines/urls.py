from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"), 


    path('', views.home, name="home"),
    path('loginHome/', views.loginHome, name="logn"),
    path('blog/', views.blog, name="blog"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('magazine/', views.magazine, name="magazine"),
    path('viewMagazine/<str:pk>/', views.viewMagazine, name="viewMagazine"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('contactUs/', views.contactUs, name="contactUs"),
    path('info/', views.info, name='info'),
    path('signIn/', views.signIn, name='signIn'),
    path('signUp/', views.signUp, name='signUp'),
    path('magazineAccessDenied/', views.magazineAccessDenied, name='magazineAccessDenied'),
    url(r'^mediumBlog/', TemplateView.as_view(template_name="medium.com/@ivisualizeyou"),
                   name='mediumBlog'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="magazines/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="magazines/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="magazines/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="magazines/password_reset_done.html"), 
        name="password_reset_complete"),

]