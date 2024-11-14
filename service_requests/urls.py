from django.urls import path
from .views import (
    CustomerListCreateView, CustomerDetailView, CustomerServiceRequestsView,
    ServiceRequestListCreateView, ServiceRequestDetailView
)

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:customer_id>/service-requests/',
         CustomerServiceRequestsView.as_view(), name='customer-service-requests'),
    path('service-requests/', ServiceRequestListCreateView.as_view(),
         name='service-request-list'),
    path('service-requests/<int:pk>/', ServiceRequestDetailView.as_view(),
         name='service-request-detail'),
]
