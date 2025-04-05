from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('add/',views.add_cart,name='add_cart'),
    path('clean/',views.clean_cart,name='clean_cart'),
    path('delete/<str:product_id>/',views.delete,name='delete'),
    path('submit/',views.submit,name='submit')
]