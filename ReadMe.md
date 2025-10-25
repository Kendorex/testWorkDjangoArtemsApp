# Куда пойти — Москва глазами Артёма

Веб-приложение для отображения интересных мест Москвы на интерактивной карте.

## Особенности

- Интерактивная карта на Leaflet с OpenStreetMap
- Пульсирующие маркеры мест
- Боковая панель с информацией о местах
- Карусель фотографий для каждого места
- Адаптивный дизайн

## Технологии

**Frontend:** Vue.js, Leaflet, Bootstrap 4  
**Backend:** Django, SQLite, REST API

##  Запуск

### Backend
python manage.py runserver

### Frontend
cd where-to-go-frontend
python -m http.server 8000

#проект запуститься на http://localhost:8000/

 API
GET /places/ - список всех мест (GeoJSON)

GET /places/<id>/ - детальная информация о месте

### Ссылка на работающий сайт
https://kendorex.pythonanywhere.com/
