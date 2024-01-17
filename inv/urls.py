from django.urls import path, include
from rest_framework import routers
from inv import views

router = routers.DefaultRouter()
router.register(r'inv',views.ProducView,'product')

urlpatterns = [
    path('inv',include(router.urls))
]
