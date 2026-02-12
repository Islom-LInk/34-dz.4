"""
URL configuration for kiki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.bolot.views import homepage_view,base_view,urmat_view,sierra_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("homepage/",homepage_view, name = "homepage-page"),
    path("", base_view, name ="base-page"),
    path("urmat/",urmat_view,name="urmat-page"),
    path("sierra/",sierra_view,name="sierra-page"),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
