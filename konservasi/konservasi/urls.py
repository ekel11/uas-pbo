"""konservasi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from konservasi_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from konservasi_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("konservasi/", konservasi),
    path("biota/", biota),
    path("add_konservasi/", add_konservasi),
    path("konservasi/edit_konservasi/<int:id>", edit_konservasi, name='edit_konservasi'),
    path("konservasi/delete_konservasi/<int:id>", delete_konservasi),
    path("add_biota/", add_biota),
    path("biota/edit_biota/<int:id>", edit_biota, name='edit_biota'),
    path("biota/delete_biota/<int:id>", delete_biota),
    path("login/", views.Pagelogin, name='login'),
    path("registrasi/", views.Pageregistrasi, name='regis'),
    path("logout/", views.Pagelogout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
