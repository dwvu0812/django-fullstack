"""
URL configuration for django_fullstack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from . import views

# Non-translatable URLs (admin, debug, language switching)
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "i18n/setlang/", views.set_language, name="set_language"
    ),  # Custom language switching
]

# Add debug toolbar for development
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

# Translatable URLs with language prefix
urlpatterns += i18n_patterns(
    path("accounts/", include("allauth.urls")),  # Allauth URLs (includes social auth)
    path(
        "auth/", include("django.contrib.auth.urls")
    ),  # Keep existing auth URLs for backward compatibility
    path("articles/", include("app.urls")),
    path("", include("app.urls")),  # Make articles the homepage
    prefix_default_language=False,  # Don't add /en/ prefix for default language
)
