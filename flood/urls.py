
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view , name ='index'),

    path('hello',views.hello,name='resultdd'),

    path('sen',views.sen,name='sen'),

    path('sensor', views.sensor_store , name ='sensor_store'),

    path('sen_update', views.sensor_update , name ='sensor_update'),

    path('value1', views.value1 , name ='sensor_value1'),

    path('value2', views.value2 , name ='sensor_value2'),

    path('value3', views.value3 , name ='sensor_value3'),

    path('value4', views.value4 , name ='sensor_value4'),
    #path('index', views.index , name ='index_view'),
    
]