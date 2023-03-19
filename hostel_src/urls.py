from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("supersecret/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



admin.site.site_header = "Patahostel Admin"
admin.site.site_title = "Patahostel Admin Portal"
admin.site.index_title = "Welcome to the Patahostel Portal"