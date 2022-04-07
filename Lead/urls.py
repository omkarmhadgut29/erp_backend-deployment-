from django.urls import path
from . import views

urlpatterns = [
    path('', views.LeadList.as_view(), name="lead"),
    path('api/add-lead/', views.AddLead.as_view(), name="add-lead"),
    path('api/delete-lead/', views.DeleteLead.as_view(), name="delete-lead"),
    path('api/update-lead/', views.UpdateLead.as_view(), name="update-lead"),
]
