from django.urls import path,include
from . import views
urlpatterns = [
    path('register/', views.UserRegistrationAPIView.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate , name ="activate"),
     path('user_type/<str:username>/', views.get_user_type_by_username, name='user_type'),
]