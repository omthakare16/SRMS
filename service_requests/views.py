from rest_framework import generics
from .models import Customer, ServiceRequest
from .serializers import CustomerSerializer, ServiceRequestSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceRequest, Customer


# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerServiceRequestsView(APIView):
    def get(self, request, customer_id):
        # Check if the customer exists
        customer = get_object_or_404(Customer, id=customer_id)

        # Fetch all service requests for this customer
        service_requests = ServiceRequest.objects.filter(customer=customer)
        
        # Serialize the service requests
        serializer = ServiceRequestSerializer(service_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

# Service Request Views
class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
