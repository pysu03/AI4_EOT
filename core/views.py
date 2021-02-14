from django.shortcuts import render
from weathers.utils import weather

# Create your views here.
def index(request):
    context = weather('서울')
    return render(request, 'core/index.html', context)