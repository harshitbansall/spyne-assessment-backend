from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ProductImage, Product, Tag

from .serializers import UserAllProductsSerializer


class UserProductsView(APIView):
    def get(self, request):

        return Response(data={
            "success": "true",
            "data": {
                "products": UserAllProductsSerializer(request.user.products.all(), many=True).data
            }
        })
