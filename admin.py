from django.contrib import admin
from .models import Kids, Sci_Fyi, Love, Story, CartItem, CartItemL, CartItemS, CartItemT, Customer, Order,Order1,Order2,Order3

@admin.register(Kids)
class KidsAdmin(admin.ModelAdmin):
    list_display=['id','Book_Name','Book_Aurthor','Book_Type','Book_Image']

@admin.register(Sci_Fyi)
class Sci_FyiAdmin(admin.ModelAdmin):
    list_display=['id','Book_Name','Book_Aurthor','Book_Type']

@admin.register(Love)
class LoveAdmin(admin.ModelAdmin):
    list_display=['id','Book_Name','Book_Aurthor','Book_Type']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display=['id','Book_Name','Book_Aurthor','Book_Type']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(CartItemL)
class CartItemLAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(CartItemS)
class CartItemLAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(CartItemT)
class CartItemTAdmin(admin.ModelAdmin):
    list_display=['user','product','quantity']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['user','address', 'city','state','pincode']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= ['id','user','customer','Kids','quantity','order_at','status']

@admin.register(Order1)
class Order1Admin(admin.ModelAdmin):
    list_display= ['id','user','customer','Love','quantity','order_at','status']

@admin.register(Order2)
class Order2Admin(admin.ModelAdmin):
    list_display= ['id','user','customer','Sci_Fyi','quantity','order_at','status']

@admin.register(Order3)
class Order2Admin(admin.ModelAdmin):
    list_display= ['id','user','customer','Story','quantity','order_at','status']
# Register your models here.
