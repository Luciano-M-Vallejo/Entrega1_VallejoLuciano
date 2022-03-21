from django.urls import path
from .views import biblography, searchBibliography

urlpatterns = [
  path('bibliography/', biblography, name='biblography'),
  path('searchBibliography/', searchBibliography , name='searchBibliography')
]
