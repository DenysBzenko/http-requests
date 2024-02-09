from django.urls import path
from . import views

urlpatterns = [
    path('cookie/set/', views.set_cookie_view),
    path('cookie/get/<str:name>/', views.get_cookie_view),
    path('header/set/', views.set_header_view),
    path('header/get/<str:name>/', views.get_header_view),
]

