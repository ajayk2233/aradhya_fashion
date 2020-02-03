from django.urls import path
from . import views

urlpatterns = [
    path('show/',views.show.as_view(),name='show'),
    path('create/',views.create.as_view(),name='create'),
    path('update/<slug:slug>',views.update.as_view(),name='update'),
    path('delete/<slug:slug>',views.delete.as_view(),name='delete'),
    path('deleteall/',views.deleteall,name='deleteall'),
]
