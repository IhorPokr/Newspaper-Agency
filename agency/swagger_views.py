from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Newspaper Agency API",
        default_version='v1',
        description="API documentation for the Newspaper Agency service.",
        terms_of_service="https://www.agency.com/terms/",
        contact=openapi.Contact(email="contact@agency.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
