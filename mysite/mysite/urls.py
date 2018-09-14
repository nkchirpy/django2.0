"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from ml import views as ml
from game import views as game
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ml.Index.as_view(), name="index"),
    path('success/', ml.Success_view.as_view(template_name="success.html")),

    path('student/', ml.Studentview.as_view(), name="student"),

    path('school/', ml.Schoolview.as_view(), name="school"),

    path('school_delete/<int:pk>', ml.Schooldeleteview.as_view(), name="school_delete"),

    path('school/<int:pk>', ml.Schoolupdateview.as_view(), name="school"),

    path('detail/', ml.detailview, name="detail"),

    path('accounts/',include('django.contrib.auth.urls')),

    path('register/',ml.register, name="register"),

    # Game's app url
    path('game/', game.game,name="game")
]
