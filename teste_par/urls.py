from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blob_api/', views.blob_api, name='blob_api'),
]