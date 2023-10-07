from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from datetime import date
from django.utils import timezone
import pytz
from django.utils import timezone
from datetime import date


# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def details_products(request):
    today = timezone.now().date()
    products = Product.objects.filter(updated_at__date=today)
    serialized_products = ProductSerializer(products, many=True).data
    
    total_price = sum(float(product['Price']) for product in serialized_products)
    count = len(serialized_products)

    response_data = {
        "products": serialized_products,
        "total_price": total_price,
        "count": count
    }

    return Response(response_data)