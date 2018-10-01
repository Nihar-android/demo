from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^player/$', views.PlayerPageView.as_view(), name='player'),
    url(r'^algorithm/$', views.algorithmPageView.as_view(), name='algorithm'),
    # url(r'^product/product-(?P<parameter>[\w-]+).html', 'views.product', name="product"),


]