from django.contrib import admin
from django.urls import path, include
from bureauinfoapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('profile/', views.profile, name='profile'),
    path('step/', views.step, name='step'),
    path('viewprofile/<int:id>/', views.viewprofile, name='viewprofile'),
    path('submitted/', views.save, name='save'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete<int:id>/', views.delete, name='delete'),
    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='log'),
    path('auth/', include('social_django.urls', namespace='social')),


]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
