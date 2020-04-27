from django.conf.urls import url
from .views import checkout, user_order


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^user_order', user_order, name='user_order'),
]
