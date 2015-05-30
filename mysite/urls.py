"""mysite URL Configuration

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

from django.conf.urls import include, url, patterns
from django.contrib import admin
from views import IndexView
from views import MasterAdd, MasterDelete, ServiceAdd, ServiceDelete, ServicesOfMastersAdd, ServicesOfMastersDelete, BookingAdd, BookingDelete

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', IndexView.as_view())
# ]


urlpatterns = patterns ('',

    url(r'^master', MasterAdd.as_view()),
    url(r'^name_delete', MasterDelete.as_view()),
    url(r'^service', ServiceAdd.as_view()),
    url(r'^deleteService', ServiceDelete.as_view()),
    url(r'^som', ServicesOfMastersAdd.as_view()),
    url(r'^deleteSom', ServicesOfMastersDelete.as_view()),
    url(r'^bo', BookingAdd.as_view()),
    url(r'^deleteBo', BookingDelete.as_view()),

    url(r'^$', IndexView.as_view()),

)

