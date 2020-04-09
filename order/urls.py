
from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('to-checkout/', views.ToCheckout.as_view(), name='to-checkout'),
    # path('complete/', views.CompleteView.as_view(), name='complete'),
    path('complete/<int:order_no>/', views.CompleteView.as_view(), name='complete'),
    path('make-order/', views.MakeOrder.as_view(), name='make-order'),
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.Shippings, name='shipping'),
    path('shipping-show/', views.ShippingShow, name='shipping-show'),
    path('shipping-update/<int:pk>', views.Shipping_update, name='shipping-update'),
    path('shipping-delete/<int:pk>', views.Shipping_delete, name='shipping-delete'),

    # path('product/<int:pk>', views.CategoryDetail.as_view(), name='list'),
    # path('cart/', views.CartList.as_view(), name='cart'),
    # path('product/detail/<int:pk>/', views.ProductDetail.as_view(), name='detail'),
    # path('cart/add/', views.add_cart, name='add-cart'),
    # path('cart/delete-one/', views.cart_delete_one, name='cart-delete-one'),
    # path('cart/delete-all/', views.cart_delete_all, name='cart-delete-all'),
]
