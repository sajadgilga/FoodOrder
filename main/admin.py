from django.contrib import admin

# Register your models here.
from main.models import Food, Order


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'create_date', 'picture', 'image_tag')
    list_filter = ('create_date',)
    search_fields = ('name', 'description', 'create_date',)

@admin.register(Order) #it is like admin.site.register(Order, OrderAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('food', 'user', 'date')
    list_filter = ('user', 'date')
    search_fields = ('user',)

admin.site.register(Food, FoodAdmin)