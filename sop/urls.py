from django.urls import path, include
from rest_framework import routers
from inv import views

router = routers.DefaultRouter()
router.register(r'sop',views.ProducView,'orders')
router.register(r'sop',views.ProducView,'order_items')
router.register(r'sop',views.ProducView,'customers')

urlpatterns = [
    path('sop',include(router.urls))
]

