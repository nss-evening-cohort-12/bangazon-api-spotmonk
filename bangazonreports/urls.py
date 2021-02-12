from django.urls import path
<<<<<<< HEAD
from .views import expensive_list, completed_order_list
=======
from .views import expensive_list, Cheap_list, completed_order_list
>>>>>>> parent of 945e7a6... removed commit from previous pr

urlpatterns = [
    path('reports/expensive', expensive_list),
    path('reports/orders/completed', completed_order_list)
]
