from django.urls import path
from . import views
from .views import register_user, login_user, logout_user

urlpatterns = [
    path('register/',views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('', views.home, name='home'),
    path('workouts/', views.workout_list, name='workout_list'),
    path('add-workout/', views.add_workout, name='add_workout'),
    path('delete-workout/<int:id>/', views.delete_workout, name='delete_workout'),
    
    path('diets/', views.diet_list, name='diet_list'),
    path('add-diet/', views.add_diet, name='add_diet'),
    path('delete-diet/<int:id>/', views.delete_diet, name='delete_diet'),
    path('login', views.login, name='login'),

]
