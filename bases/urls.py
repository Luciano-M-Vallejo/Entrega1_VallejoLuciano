from django.urls import path
# from .views import biblography, searchBibliography, creatBiblography, blogs, userInfo
from . import views

urlpatterns = [
  
  path('listBibliography/', views.listBiblography, name='listBibliography'),
  path('creatBibliography/', views.creatBiblography, name='creatBibliography'),
  path('upLoadBibliography/<int:id>/', views.upLoadBibliography, name='upLoadBibliography'),
  path('deleteBibliography/<int:id>/', views.deleteBibliography, name='deleteBibliography'),
  path('searchBibliography/', views.searchBibliography , name='searchBibliography'),
  
  path('blogs/', views.blogs , name='blogs'),
  path('creatBlog/', views.creatBlog, name='creatBlog'),
  
  path('userInfo/', views.userInfo , name='userInfo')
]
