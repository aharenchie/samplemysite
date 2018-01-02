from django.urls import path
from upload_form import views

app_name = 'upload_form'
urlpatterns = [
    #url(r'^$', views.form, name = 'form'),
    #url(r'^complete/', views.complete, name = 'complete'),
    path('', views.form, name = 'form'),
    path('complete/', views.complete, name = 'complete'),
]
