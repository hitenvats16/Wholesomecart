from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='AboutUs'),
    path('tracker',views.tracker,name='Tracker'),
    path('contact',views.contact,name='Contact'),
    path('search',views.search,name='Search'),
    path('product_view/<str:id>',views.product_view,name='ProductView'),
    path('checkout/<str:id>',views.checkoutSingleProduct,name='Checkout'),
    path('checkout',views.checkoutMultiProd,name='checkoutmulti'),
    path('conformation',views.conformation,name='conformation'),
]

