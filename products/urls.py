from django.urls import path

from .views import ProductListView, ProductDetailView

# from .views import ...

urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
