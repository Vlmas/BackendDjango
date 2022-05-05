import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.product import Product
from api.serializers.product import ProductSerializer

logger = logging.getLogger(__name__)


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        data = serializer.data
        logger.debug(f'Products GET {data}')
        return Response(data, status=http.HTTPStatus.OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug(f'Products POST {data}')
            return Response(data, http.HTTPStatus.CREATED)
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class ProductDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        data = serializer.data
        logger.debug(f'Product by ID GET {data}')
        return Response(data, http.HTTPStatus.OK)

    def put(self, request, pk):
        serializer = ProductSerializer(data=request.data)
        product = self.get_object(pk)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug(f'Products PUT {data}')
            return Response(data, http.HTTPStatus.ACCEPTED)
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response({
            'message': 'product deleted'
        }, status=http.HTTPStatus.OK)


class ProductByCategoryAPIView(APIView):
    def get_objects(self, category_name):
        try:
            return Product.category_related.get_products_by_category(category_name)
        except Product.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, category_name):
        products = self.get_objects(category_name)
        serializer = ProductSerializer(products)
        data = serializer.data
        logger.debug(f'Products by category GET {data}')
        return Response(data, http.HTTPStatus.OK)

