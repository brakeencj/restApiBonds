from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from bonds import views

router = DefaultRouter()
router.register(r'bonds', views.BondViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
