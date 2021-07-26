from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from bonds import views

router = DefaultRouter()
router.register(r'bonds', views.BondViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'purchased', views.PurchaseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
]
