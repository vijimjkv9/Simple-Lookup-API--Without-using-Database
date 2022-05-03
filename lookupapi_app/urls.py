from django.urls import path, include
from rest_framework import routers
from .views import DepartmentViewSet

router = routers.DefaultRouter()
router.register('department', DepartmentViewSet,
                basename='department')
urlpatterns = [
    path('', include(router.urls)),
]
