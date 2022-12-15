from django.urls import path
from . import views


urlpatterns = [
    path("", views.store, name="store"),
    # === SORT PRODUCT BY CATEGORY === #
    path("category/<slug:category_slug>/", views.store, name="products_by_category"),
    # === PRODUCT DETAIL === #
    path("category/<slug:category_slug>/<slug:product_slug>/", views.product_detail, name="product_detail"),
    # === SEARCH PRODUCTS === #
    path("search/", views.search, name="search"),
]