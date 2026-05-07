from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('journal.urls')), # This tells Django to check your journal app
]