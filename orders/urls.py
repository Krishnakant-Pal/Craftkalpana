from django.urls import path
from . import views
urlpatterns = [
    path('order-placed',views.order_place,name="order_placed"),
    path('payments/', views.payments, name='payments'),
]