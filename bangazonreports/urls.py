from django.urls import path
from .views import expensive_list

urlpatterns = [
    path('reports/expensive', expensive_list),
]
