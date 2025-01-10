from django.urls import path
from . import views


urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('movie/<str:pk>/',views.movie, name='movie'),
    path('my-list', views.my_list, name='my-list'),

    path('add-to-list',views.add_to_list,name='add-to-list'),
    path('search',views.search,name='search'),
    path('genre/<str:pk>/',views.genre, name='genre'),
    path('admin-add-movies/', views.admin_add_movies, name='admin-add-movies'),
    path("add", views.add, name="add"),                                 # Add new admin

    path('admin-view-page/',views.admin_view_page,name='admin-view-page'),
    path('admin-view-users/',views.admin_view_users,name='admin-view-users'),





] 