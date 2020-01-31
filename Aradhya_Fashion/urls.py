from django.contrib import admin
from django.urls import path,include
app_name='darjano'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('darjano/',include('darjano.urls')),
]
