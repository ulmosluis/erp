from django.urls import path, include
from rest_framework import routers
from sop import views

router = routers.DefaultRouter()
router.register(r'sop',views.OrderView,'orders')
router.register(r'sop',views.OrderItemView,'order_items')
router.register(r'sop',views.CustomerView,'customers')

urlpatterns = [
    path('sop/',include(router.urls))
]

