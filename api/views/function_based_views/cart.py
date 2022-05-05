import logging
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from api.models.cart import Cart
from api.serializers.cart import CartSerializer

logger = logging.getLogger(__name__)
authentication_classes = (TokenAuthentication,)
permission_classes = (IsAuthenticated,)


@api_view(['GET', 'POST'])
def cart_list(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        data = serializer.data
        logger.log(123, data)
        return Response(data)

    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def cart_details(request, cart_id, product_id=None):
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist as exc:
        return Response({
            'message': 'invalid id',
        }, status=400)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        data = serializer.data
        return Response(data)


@api_view(['GET', 'POST'])
def cart_products(request, cart_id):
    try:
        cart = Cart.objects.get(id=cart_id)
    except Cart.DoesNotExist as exc:
        return Response({
            'message': 'invalid id',
        }, status=400)

    if request.method == 'GET':
        return cart.products
