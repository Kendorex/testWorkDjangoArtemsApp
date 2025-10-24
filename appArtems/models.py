from django.db import models
from ckeditor.fields import RichTextField

class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название места")
    place_id = models.CharField(max_length=100, unique=True, verbose_name="ID места", blank=True, null=True)
    description_short = models.TextField(verbose_name="Краткое описание", blank=True)
    description_long = RichTextField(verbose_name="Полное описание", blank=True)
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")
    
    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"
    
    def __str__(self):
        return self.title

class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place, 
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Локация"
    )
    image = models.ImageField(upload_to='places/', verbose_name="Изображение")
    position = models.PositiveIntegerField(default=0, verbose_name="Позиция")
    
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['position']
    
    def __str__(self):
        return f"Изображение для {self.place.title}"
    
