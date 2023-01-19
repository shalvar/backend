
from django.contrib import admin
from django.urls import path,include,re_path
from core.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('(?P<lang>(ru|en))/', include(router.urls)),
]

