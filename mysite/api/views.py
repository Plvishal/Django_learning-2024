from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
# Create your views here.
class ItemsViewSet(viewsets.ModelViewSet):
    print("Hello i am called*************")
    queryset=Item.objects.all()
    serializer_class=ItemSerializer
    
