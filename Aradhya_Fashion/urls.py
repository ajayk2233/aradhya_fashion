from django.contrib import admin
from django.urls import path,include
from adminpanel.admin import admin_site
app_name='darjano'
urlpatterns = [
    path('admin/', admin_site.urls),
    path('darjano/',include('darjano.urls')),
]
