from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views.function_based_views.cart import *
from api.views.function_based_views.guidebook import *
from api.views.class_based_views.sign_up import SignUpView
from api.views.class_based_views.product import *
from api.views.class_based_views.category import *
from api.views.class_based_views.user import *

router = routers.DefaultRouter()

urlpatterns = [
    path('/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('sign-up/', SignUpView.as_view()),

    path('carts/', cart_list),
    path('carts/<int:cart_id>/', cart_details),
    path('carts/<int:cart_id>/products/', cart_products),

    path('products/', ProductListAPIView.as_view()),
    path('products/<int:product_id>/', ProductDetailsAPIView.as_view()),

    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<str:name>/', CategoryDetailsAPIView.as_view()),
    path('categories/<str:name>/products/', CategoryProductsAPIView.as_view()),

    path('users/', UserListAPIView.as_view()),
    path('users/<int:user_id>/', UserDetailsAPIView.as_view()),
    path('users/<int:user_id>/cart/', CartByUserAPIView.as_view()),

    path('guidebooks/', guidebook_list),
    path('guidebooks/<int:guidebook_id>/', guidebook_details),
    path('guidebooks/<int:guidebook_id>/content/', guidebook_content),
]
