from django.contrib import admin
from django.urls import path,include
from .views import *
from api.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_page),
    path('', home_page),
    path('api/v1/',include('api.urls'))
]
