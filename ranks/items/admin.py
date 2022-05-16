from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'price',
    )
    list_editable = ('name', 'description', 'price',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Item, ItemAdmin)
