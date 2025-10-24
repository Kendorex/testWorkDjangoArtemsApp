from django.shortcuts import render
from django.utils import timezone

def home_page(request):
    context = {
        'current_time': timezone.now()
    }
    return render(request, 'index.html', context)