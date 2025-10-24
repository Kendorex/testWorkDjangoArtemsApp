from django.utils.html import mark_safe
from django.contrib import admin
from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)
    ordering = ('position',)
    
    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            try:
                return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
            except:
                return "Ошибка загрузки изображения"
        return "Нет изображения"
    image_preview.short_description = "Предпросмотр"

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lat', 'lng')
    list_filter = ('title',)
    search_fields = ('title', 'description_short')
    inlines = [PlaceImageInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'description_short', 'description_long')
        }),
        ('Координаты', {
            'fields': ('lat', 'lng')
        }),
    )

@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'position', 'image_preview')
    list_filter = ('place',)
    readonly_fields = ('image_preview',)
    ordering = ('position',)
    
    def image_preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            try:
                return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; max-width: 100px;" />')
            except:
                return "Ошибка загрузки изображения"
        return "Нет изображения"
    image_preview.short_description = "Предпросмотр"