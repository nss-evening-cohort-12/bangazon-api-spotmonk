from django.urls import path
from .views import expensive_list, completed_order_list

urlpatterns = [
    path('reports/expensive', expensive_list),
    path('reports/orders/completed', completed_order_list)
