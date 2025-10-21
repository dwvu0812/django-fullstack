from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import translate_url
from django.utils.translation import check_for_language
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@never_cache
@csrf_exempt
@require_POST
def set_language(request):
    """
    Custom language switching view that handles URL redirects properly
    for both prefixed and non-prefixed language URLs.
    """
    language = request.POST.get("language")
    if not language:
        language = request.GET.get("language")

    if language and check_for_language(language):
        # Get the current URL
        next_url = request.POST.get("next", request.GET.get("next"))
        if not next_url:
            next_url = request.META.get("HTTP_REFERER")
        if not next_url:
            next_url = "/"

        # Handle language switching logic
        if language == settings.LANGUAGE_CODE:
            # Switching to default language (English) - remove language prefix
            if next_url.startswith("/vi/"):
                next_url = next_url[3:]  # Remove /vi/ prefix
            elif next_url.startswith("/en/"):
                next_url = next_url[3:]  # Remove /en/ prefix if present
            # Make sure we don't have double slashes
            if not next_url.startswith("/"):
                next_url = "/" + next_url
        else:
            # Switching to non-default language (Vietnamese) - add language prefix
            if next_url.startswith("/vi/"):
                # Already has Vietnamese prefix, keep it
                pass
            elif next_url.startswith("/en/"):
                # Replace /en/ with /vi/
                next_url = f"/vi{next_url[3:]}"
            else:
                # Remove any existing language prefix and add Vietnamese prefix
                # Handle URLs that might start with other language codes
                url_parts = next_url.strip("/").split("/")
                if len(url_parts) > 0 and len(url_parts[0]) == 2:
                    # Might be a language code, remove it
                    next_url = (
                        "/" + "/".join(url_parts[1:]) if len(url_parts) > 1 else "/"
                    )

                # Add Vietnamese prefix
                if not next_url.startswith("/"):
                    next_url = "/" + next_url
                next_url = f"/vi{next_url}"

        # Ensure the URL starts with /
        if not next_url.startswith("/"):
            next_url = "/" + next_url

        # Set the language in session
        request.session["django_language"] = language

        response = HttpResponseRedirect(next_url)
        response.set_cookie(
            "django_language",
            language,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
        return response

    # Fallback to home page if language is invalid
    return HttpResponseRedirect("/")
