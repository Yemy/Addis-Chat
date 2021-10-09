from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),

    path('user/profile/', user_views.profile, name='profile'),    
    path('user/', include('users.urls')),
]
