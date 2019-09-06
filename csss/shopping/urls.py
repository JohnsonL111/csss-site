"""csss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.print_catalogue, name='print_catalogue'),
    url(r'^add_item_to_cart/', views.add_item_to_cart, name='add_item_to_cart'),
    url(r'^checkout_form/', views.checkout_form, name='checkout_form'),
    url(r'^remove/', views.remove_item, name='remove_item'),
]