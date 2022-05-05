import http
import logging
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.cart import Cart
from api.models.user import User
from api.serializers.cart import CartSerializer
from api.serializers.user import UserSerializer

logger = logging.getLogger(__name__)


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = serializer.data
        logger.debug(f'Users GET {data}')
        return Response(data, status=http.HTTPStatus.OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            logger.debug(f'Users POST {data}')
            return Response(data, http.HTTPStatus.CREATED)
        return Response(serializer.errors, http.HTTPStatus.BAD_REQUEST)


class UserDetailsAPIView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        data = serializer.data
        logger.debug(f'User by ID GET {data}')
        return Response(data, http.HTTPStatus.OK)


class CartByUserAPIView(APIView):
    def get_object(self, cart_id):
        try:
            return Cart.objects.get(cart_id=cart_id)
        except Cart.DoesNotExist:
            raise http.HTTPStatus.NOT_FOUND

    def get(self, request, cart_id):
        cart = self.get_object(cart_id)
        serializer = CartSerializer(cart)
        data = serializer.data
        logger.debug(f'Cart by User ID GET {data}')
        return Response(data, http.HTTPStatus.OK)