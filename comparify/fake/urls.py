from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
# path('results/',views.results,name='results'),
path('results2/',views.results2,name='results2')
]