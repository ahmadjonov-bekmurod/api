from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="ToDoAppAPI",
        description="To Do App API",
        default_version="v1",
        terms_of_service="https://www.google.com",
        contact=openapi.Contact(email="ahmoadjonovbekmurod06@gmail.com"),
        license=openapi.License(name="ToDoApp.com license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path('admin', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('', include('accounts.urls')),
    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0)),
    path('redoc', schema_view.with_ui(
        'redoc', cache_timeout=0))
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
