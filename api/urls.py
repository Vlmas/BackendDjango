from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.function_based_views.cart import *
from api.views.class_based_views.product import *

router = routers.DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('carts/', cart_list),
    path('carts/<int:cart_id>/', cart_details),
    path('carts/<int:cart_id>/products', cart_products),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>', ProductDetailsAPIView.as_view()),
    path('products/<str:category_name>', ProductByCategoryAPIView.as_view()),


]
