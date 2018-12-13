from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    path('', include('mirari.mirari.urls')),
    path('SV/', include('mirari.SV.urls')),
    path('INT/', include('mirari.INT.urls')),
    path('CRYE/', include('mirari.CRYE.urls')),
    path('TCS/', include('mirari.TCS.urls')),

    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-verify/', verify_jwt_token),

    path(settings.ADMIN_URL, admin.site.urls),
    #path("accounts/", include("allauth.urls")),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path("400/",default_views.bad_request,kwargs={"exception": Exception("Bad Request!")},),
        path("403/",default_views.permission_denied,kwargs={"exception": Exception("Permission Denied")},),
        path("404/",default_views.page_not_found,kwargs={"exception": Exception("Page not Found")},),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
else:
    handler404 = 'mirari.mirari.views.View400'
    handler500 = 'mirari.mirari.views.View403'
    handler403 = 'mirari.mirari.views.View404'
    handler400 = 'mirari.mirari.views.View500'
