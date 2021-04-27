from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Tech-Chat"
admin.site.site_title = "Tech Group.inc"
admin.site.index_title = "Tech Chat"


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]
