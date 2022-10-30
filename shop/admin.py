from django.contrib import admin
from shop.models import Contact, Order, Product, Tracker

admin.site.register([Product,Contact,Order,Tracker])
