from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, start_thread


app_name = 'messenger'
urlpatterns = [
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='detail'),
    path('thread/<int:pk>/add', add_message, name='add'),
    path('thread/start/<str:username>/', start_thread, name='start')
]