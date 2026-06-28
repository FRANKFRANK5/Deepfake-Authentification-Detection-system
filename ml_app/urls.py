"""
project_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import about, index, predict_page, video_upload_api, result, get_data
from .views import login_view, register_view, logout_view  # <-- ONGEZA HII
from project_settings import settings
from django.conf.urls.static import static

app_name = 'ml_app'
handler404 = views.handler404

urlpatterns = [
    # Home and info pages
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('predict/', predict_page, name='predict'),
    path('result/', result, name='result'),
    
    # API endpoints
    path('video_upload_api/', video_upload_api, name='video_upload_api'),
    path('get_data/', get_data, name='get_data'),
    
    # ============================================
    # AUTHENTICATION - NYONGEZA HAPA CHINI
    # ============================================
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]

# Media files (zilizopo)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)