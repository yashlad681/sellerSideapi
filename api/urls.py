from django.urls import path
from . import views

urlpatterns = [
    path('seller/signup',views.SignupAPI.as_view(),name='seller_signup'),
    path('seller/store/create',views.StoreCreationAPI.as_view(),name='seller_create_store'),
    path('seller/inventory/upload',views.InventoryUploadAPI.as_view(),name='seller_upload_inventory'),
    path('seller/order/accept',views.OrderAcceptView.as_view(),name='seller_accept_order'),
]