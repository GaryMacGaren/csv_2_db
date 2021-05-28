from rest_framework.viewsets import ModelViewSet
from .serializer import SerializeCustomer
from .models import Customer

class CustomerModelViewSet(ModelViewSet):
    model = Customer
    serializer_class = SerializeCustomer
    queryset = Customer.objects.all()
