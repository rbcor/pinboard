from django.conf.urls import url
from django.contrib import admin

from pinboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]


urlpatterns +=[
    url(r'^$', views.IndexListView.as_view(), name= 'index'),
    url(r'^(?P<pk>\d+)/$', views.PinDetailView.as_view() , name='detail'),
]