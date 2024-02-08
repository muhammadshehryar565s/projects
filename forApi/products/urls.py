from django.urls import path,include
from . import views
from products.views import categoryViewSet,productViewSet,ProductDetailViewSet,addtocartViewSet,displaycartViewSet
from rest_framework import routers
from django.views.generic.base import View
from . import views

router=routers.DefaultRouter()
router.register(r'category',categoryViewSet)
router.register(r'product', productViewSet)

router.register(r'product-details', ProductDetailViewSet)
router.register(r'addtocart',addtocartViewSet)
router.register(r'displaycart',displaycartViewSet)


urlpatterns = [
    
    path("api/v1/",include(router.urls)),
    
    # path('product/<str:cat_slug>/<str:pro_slug>/',views.getList.as_view())
    # path('product/<str:slug>/<int:id>',views.product_detail())
    # path('api/products/<slug:pro_slug>/<slug:cat_slug>/', views.ProductDetail.as_view(), name='product-detail'),
    # path('/api/v1/product-details/<slug:pro_slug>/<int:product_id>/', views.ProductDetail.as_view(), name='product-detail'),
    # path("api/v1/", include(router.urls)),
    # path("api/v1/", include(router.urls)),
]
  