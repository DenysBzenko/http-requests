from django.urls import path
from . import views



urlpatterns = [
    path('cookie/set/', views.set_cookie_view),
    path('cookie/get/<str:name>/', views.get_cookie_view),
    path('header/set/', views.set_header_view),
    path('header/get/<str:name>/', views.get_header_view),

    path('users/', views.get_all_users, name='get_all_users'),
    path('users/<int:id>/', views.get_user_by_id, name='get_user_by_id'),
    path('users/new/', views.post_user, name='post_user'),
    path('users/update/<int:id>/', views.put_user, name='put_user'),
    path('users/modify/<int:id>/', views.patch_user, name='patch_user'),
    path('users/delete/<int:id>/', views.delete_user, name='delete_user'),
    path('users/admins/', views.get_admin_users, name='get_admin_users'),
]
