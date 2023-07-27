from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include your app's URLs here
    path('text/', include('text.urls')),
]