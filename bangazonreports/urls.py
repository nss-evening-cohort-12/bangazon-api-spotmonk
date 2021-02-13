from django.urls import path
from .views import expensive_list, Cheap_list, completed_order_list, incomplete_order_list, favorites_list

urlpatterns = [
    path('reports/expensive', expensive_list),
    path('reports/orders/completed', completed_order_list),
    path('reports/cheap', Cheap_list),
    path('reports/orders/incomplete', incomplete_order_list),
    path('reports/favorites', favorites_list)
]
