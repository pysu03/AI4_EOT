from django.contrib import admin
from django.urls    import path, include
from weathers       import views
urlpatterns = [
    path('index/',      views.index,        name='index'),
    path('search/',     views.search,       name='search'),
    path('weather/',    views.weather,      name='weather'),

]