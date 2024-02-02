"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

api_path = 'api/v1'

urlpatterns = [
    path("admin/", admin.site.urls),

    # DRF - Django Rest Framework
    path('api-auth/', include('rest_framework.urls')),
    path(f"{api_path}/client/", include(("client.urls_api", "user-api"), namespace="user-api")),
    path(f"{api_path}/document/", include(("document.urls_api", "user-api"), namespace="user-api")),
    path(f"{api_path}/payment/", include(("payment.urls_api", "user-api"), namespace="user-api")),
    path(f"{api_path}/invoice/", include(("invoice.urls_api", "invoice-api"), namespace="invoice-api")),
    path(f"{api_path}/project/", include(("project.urls_api", "project-api"), namespace="project-api")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



