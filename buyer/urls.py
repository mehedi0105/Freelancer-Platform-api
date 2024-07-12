from django.urls import path
from . import views
urlpatterns = [
    path('job_list/', views.All_JOB_LIST_API_VIEW.as_view(),name='job_list' ),
    path('job_details/<int:pk>/', views.JOB_DETAILS_API_VIEW.as_view(), name='job_details'),
    path('reveiw/<int:pk>/', views.ReveiwListAPIView.as_view(),name='reveiw'),
    path('reveiw/', views.AllReveiwListAPIView.as_view(),name='all_reveiw'),
    path('category/', views.AllCategoryListAPIView.as_view(),name='category'),
    path('category/serch/<str:category_slug>/',views.CategorySlugListAPIView.as_view(), name='CategorySlugListAPIView'),
]
