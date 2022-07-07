from django.urls import path, include
from .viewsets import ClientViewSet, DeviceViewSet
from .views import LoanListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'device', DeviceViewSet)

urlpatterns = [
    path('loan/', LoanListView.as_view()),
    path('', include(router.urls))
]

