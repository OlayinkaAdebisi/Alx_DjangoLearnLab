"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_list/',views.funct_view, name='book_list'),
    path('class_view/',views.class_view.as_view(),name ='class_view'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("signup/", views.register.as_view(), name="register"),
    path('admin_view/',admin_view,name='admin_view'),
    path('librarian_view/',librarian_view,name='librarian_view'),
    path('member_view/',member_view,name='member_view'),

]
