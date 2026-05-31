from django.urls import path
from . import views

urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('add/', views.PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/edit/', views.PatientUpdateView.as_view(), name='patient_update'),
    path('<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient_delete'),
]
