# appArtems/management/commands/load_initial_data.py
import json
from django.core.management.base import BaseCommand
from django.core.files import File
import requests
from io import BytesIO
from appArtems.models import Place, PlaceImage

class Command(BaseCommand):
    help = 'Load initial data from frontend template'
    
    def handle(self, *args, **options):
        # Данные из GeoJSON в шаблоне
        places_data = [
            {
                "place_id": "moscow_legends",
                "title": "«Легенды Москвы»",
                "lng": 37.62,
                "lat": 55.793676,
                "details_url": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            },
            {
                "place_id": "roofs24", 
                "title": "Крыши24.рф",
                "lng": 37.64,
                "lat": 55.753676,
                "details_url": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
            }
        ]
        
        for place_info in places_data:
            # Загружаем детальную информацию
            response = requests.get(place_info['details_url'])
            details = response.json()
            
            # Создаем локацию
            place, created = Place.objects.get_or_create(
                place_id=place_info['place_id'],
                defaults={
                    'title': details['title'],
                    'description_short': details.get('description_short', ''),
                    'description_long': details.get('description_long', ''),
                    'lng': place_info['lng'],
                    'lat': place_info['lat']
                }
            )
            
            if created:
                self.stdout.write(f"Created place: {place.title}")
                
                # Загружаем изображения
                for img_url in details.get('imgs', []):
                    try:
                        response = requests.get(img_url)
                        response.raise_for_status()
                        
                        # Создаем имя файла из URL
                        filename = img_url.split('/')[-1]
                        
                        # Создаем изображение
                        place_image = PlaceImage(place=place)
                        place_image.image.save(
                            filename,
                            File(BytesIO(response.content)),
                            save=True
                        )
                        self.stdout.write(f"  Added image: {filename}")
                        
                    except Exception as e:
                        self.stdout.write(f"  Error loading image {img_url}: {e}")
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded initial data'))