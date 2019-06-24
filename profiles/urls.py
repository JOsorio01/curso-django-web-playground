from django.urls import path
from .views import ProfilesList, ProfileDetail


app_name = 'profiles'
urlpatterns = [
    path('', ProfilesList.as_view(), name='profiles'),
    path('<str:username>/', ProfileDetail.as_view(), name='detail'),
]