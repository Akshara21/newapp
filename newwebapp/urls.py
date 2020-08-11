
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', include('newpg.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='userpg/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='userpg/logout.html'), name='logout'),
    path('new/', include('userpg.urls')),
]
