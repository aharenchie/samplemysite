from django.urls import path
from .views import PersonCreateView,PersonListView

app_name = 'imgfix'
urlpatterns = [
    path('', PersonListView.as_view()),
    path('create/', PersonCreateView.as_view())
]    
