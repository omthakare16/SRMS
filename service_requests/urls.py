from django.urls import path
from .views import (
    CustomerListView,
    create_service_request,
    ServiceRequestDetailTemplateView,
    customer_service_requests,
    CustomerListCreateView,
    CustomerDetailView,
    CustomerServiceRequestsView,
    ServiceRequestListCreateView,
    ServiceRequestDetailView
)

urlpatterns = [
    # API Endpoints
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/<int:customer_id>/service-requests/',
         CustomerServiceRequestsView.as_view(), name='customer-service-requests'),
    path('service-requests/', ServiceRequestListCreateView.as_view(),
         name='service-request-list'),
    path('service-requests/<int:pk>/', ServiceRequestDetailView.as_view(),
         name='service-request-detail'),

    # Django Template Views
    path('customers/list/', CustomerListView.as_view(), name='customer-list-template'),
    path('service-requests/new/', create_service_request, name='service-request-form'),
    path('service-requests/<int:pk>/detail/',
         ServiceRequestDetailTemplateView.as_view(), name='service-request-detail-template'),
]
