from django.urls import path
from api.views import (
    BuyView, ItemView, SuccessView,
    CancelView, CreateOrderView, ItemsView
)


app_name = 'api'


urlpatterns = [
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
    path('item/<int:id>/', ItemView.as_view(), name='item'),
    path('items/', ItemsView.as_view(), name='item'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('order/', CreateOrderView.as_view(), name='create'),
]
