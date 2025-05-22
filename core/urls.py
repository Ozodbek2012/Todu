from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentlar/', studentlar_view, name='studentlar'),
    path('reja/', Reja_view, name='Reja' ),
    path('reja/ochir/<int:reja_id>/', reja_ochir, name='reja_ochir'),


]
