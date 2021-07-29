from django.conf.urls import include, url
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from bonds import views

router = DefaultRouter()
router.register(r'bonds', views.BondViewSet)
router.register(r'users', views.UserViewSet)


schema_view = get_schema_view(
    openapi.Info(
        title="Bonds API",
        default_version='v1',
        description="Challenge project",
        terms_of_service="https://github.com/brakeencj/restApiBonds",
        contact=openapi.Contact(email="brakeencj@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]
