from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shuru/', home, name='start'),
    path('dynamic/', include('dynamic.urls'))
]
