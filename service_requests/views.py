from rest_framework import generics
from .models import Customer, ServiceRequest
from .serializers import CustomerSerializer, ServiceRequestSerializer
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import ServiceRequestForm
from django.views.generic import ListView, FormView, DetailView

# ----------------- API Views -----------------

# Customer Views
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerServiceRequestsView(APIView):
    def get(self, request, customer_id):
        customer = get_object_or_404(Customer, id=customer_id)
        service_requests = ServiceRequest.objects.filter(customer=customer)
        serializer = ServiceRequestSerializer(service_requests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Service Request Views
class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

# ----------------- Template Views -----------------

# Customer List View (Template)
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

# Service Request Form View (Template)
def create_service_request(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = customer
            service_request.save()
            return redirect('customer-service-requests', customer_id=customer.id)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form, 'customer': customer})

# Service Request Detail View (Template)
class ServiceRequestDetailTemplateView(DetailView):
    model = ServiceRequest
    template_name = 'service_requests/service_request_detail.html'
    context_object_name = 'service_request'

# View to Display Customer's Service Requests (Template)
def customer_service_requests(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    service_requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'customers/service_requests.html', {
        'customer': customer,
        'service_requests': service_requests
    })
