from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    path('index/',views.index , name='index'),
    path('list/',views.post_list,name='post_list'),
    path('detail/<int:pk>/<slug:slug>/<int:year>/<int:month>/<int:day>/',views.post_detail,name='post_detail'),
]
