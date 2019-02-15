from django.contrib import admin
from django.conf.urls import url
from django.urls import path , include
from rest_framework import routers
from rest_framework import routers
from dvdrental.views import *

from . import views
rout = routers.DefaultRouter()
#rout.register(r'actor',views.actorViewSet)
rout.register(r'actor_name', actorViewSet)
rout.register(r'actor_name_like', actorViewSet2)
rout.register(r'actor_name_upper', actorViewSet3)
rout.register(r'last_name_GEN', actorViewSet4)
rout.register(r'last_name_LI', actorViewSet5)
rout.register(r'country_name', countryViewSet)
rout.register(r'add_column', actorViewSet6)
rout.register(r'count_last_name', actorViewSet7)
rout.register(r'join', film_actorViewSet)




urlpatterns = [

    #path('problem_1/', views.actorViewSet)
   # path('tests/', include(rout.urls)),
    path(r'', include(rout.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    ]