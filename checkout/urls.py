from django.conf.urls import url
from .views import checkout, user_order


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^order_history', user_order, name='user_order'),
]
