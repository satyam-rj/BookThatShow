"""
URL configuration for verditales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import view

urlpatterns = [
    path('admin_login/', view.Verditales.admin_login),
    path('admin_dashboard/<str:email>/<str:password>/', view.Verditales.admin_dashboard),
    path('add_movie/<str:email>/<str:password>/', view.Verditales.add_movie),
    path('delete_movie/<str:email>/<str:password>/<str:iid>/', view.Verditales.delete_movie),
    path('archive_status/<str:email>/<str:password>/<str:iid>/', view.Verditales.archive_movie),
    path('movies/<str:_id>/', view.Verditales.movies),
    path('', view.Verditales.index),
]