from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.MainList.as_view(), name='main_list'),
    path('main/create/', views.LowerCreate.as_view(), name='lower_create'),
    path('main/<int:pk>/update/', views.LowerUpdate.as_view(), name='lower_update'),
    path('main/<int:pk>/delete/', views.LowerDelete.as_view(), name='lower_delete'),
    path('lookup/', views.HigherView.as_view(), name='higher_list'),
    path('lookup/create/', views.HigherCreate.as_view(), name='higher_create'),
    path('lookup/<int:pk>/update/', views.HigherUpdate.as_view(), name='higher_update'),
    path('lookup/<int:pk>/delete/', views.HigherDelete.as_view(), name='higher_delete'),
]
