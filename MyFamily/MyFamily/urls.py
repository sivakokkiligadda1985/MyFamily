"""MyFamily URL Configuration

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
from django.urls import path
from website1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.fun1),
    path('Muktheswarao/',views.fun2),
    path('Janakamaharaju/',views.fun3),
    path('Nancharaiah/',views.fun4),
    path('Srinivasarao/',views.fun5),
    path('Venkateswarao/',views.fun6),
    path('Siva brothers/',views.fun7),
]
