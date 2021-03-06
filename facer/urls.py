"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'facer.views.facer_home', name='facer_home'),
    url(r'^1/$', 'facer.views.facer1_input', name='facer1_input'),
    url(r'^1/output$', 'facer.views.facer1_output', name='facer1_output'),
    #url(r'^2/$', 'facer.views.facer2_input', name='facer2_input'),
    #url(r'^2/output$', 'facer.views.facer2_output', name='facer2_output'),
]
