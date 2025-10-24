import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place

def place_detail_api(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    
    imgs = [request.build_absolute_uri(image.image.url) for image in place.images.all()]
    
    data = {
        'title': place.title,
        'imgs': imgs,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }

    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=utf-8')


def places_list_api(request):
    places = Place.objects.all()
    
    places_data = {
        "type": "FeatureCollection",
        "features": []
    }
    
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "placeId": place.id,
                "title": place.title,
                "color": "red"  # Можно задать разные цвета
            }
        }
        places_data["features"].append(feature)
    
    json_str = json.dumps(places_data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type='application/json; charset=utf-8')