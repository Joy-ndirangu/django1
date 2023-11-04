from django.urls import path
from . import views

app_name="teachers"
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('add/', views.add, name="addData"),
    path('viewdata/', views.viewdata, name="viewdata"),
    path('delete/<id>',views.delete, name="delete"),
    path('insert/', views.insertdata, name="insertdata"),
    path('edit/<id>', views.edit, name="edit"),
    path('sliders/',views.sliders, name="sliders"),
    path('search/', views.search, name="search")

]
