from django.contrib import admin
from django.urls import path,include
from firstapp import views
from demo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('firstapp.urls')),
    path('', include('demo.urls')),
]
