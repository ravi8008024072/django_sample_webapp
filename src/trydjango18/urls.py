from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'trydjango18.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^contact', 'newsletter.views.contact', name='contact'),
    url(r'^about', 'trydjango18.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', 'newsletter.views.home', name='home'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
