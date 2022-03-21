from django.urls import path
from .views import biblography, searchBibliography, blogs, userInfo

urlpatterns = [
  path('bibliography/', biblography, name='biblography'),
  path('searchBibliography/', searchBibliography , name='searchBibliography'),
  path('blogs/', blogs , name='blogs'),
  path('userInfo/', userInfo , name='userInfo')
]
