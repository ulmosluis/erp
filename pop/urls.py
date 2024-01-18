from django.urls import path, include
from rest_framework import routers
from pop import views

router = routers.DefaultRouter()
router.register(r'pop',views.SupplierView,'Supplier')

urlpatterns = [
    path('pop/',include(router.urls))
]