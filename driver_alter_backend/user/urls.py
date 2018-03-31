"""driver_alter_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.home),
    # url like start_trip/<username>
    url(r'^start_trip/(?P<user_name>\w+)/$', views.create_new_trip),
    # url like end_trip/<username>
    url(r'^end_trip/(?P<user_name>\w+)/$', views.end_trip),
    # url like post_data/<username>?v1=<value1>&v2=<value2>&v3=<value3>&v4=<value4>
    url(r'^send_data/(?P<user_name>\w+)/$', views.receive_data)
]
