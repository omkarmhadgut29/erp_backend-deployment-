from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name="customer"),
    path('api/add-customer/', views.AddCustomer.as_view(), name="add-customer"),
    path('api/delete-customer/', views.DeleteCustomer.as_view(), name="delete-customer"),
    path('api/update-customer/', views.UpdateCustomer.as_view(), name="update-customer"),
    path('api/customer/churn/', views.CustomerPredictionDataSetList.as_view(), name="customer_churn"),
    path('api/customer/churn/add/', views.AddCustomerPredictionDataSet.as_view(), name="add_churn"),
    path('api/customer/churn/delete/', views.CustomerDeletePredictionDataSet.as_view(), name="delete_churn"),
]
