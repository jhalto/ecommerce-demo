from django.urls import path
from .views import product_detail_view


urlpatterns = [
    path("<int:id>", view= product_detail_view, name= 'product_detail_view')
]