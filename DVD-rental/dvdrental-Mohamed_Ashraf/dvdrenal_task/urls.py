"""dvdrenal_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from dvdrenal_app import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'actor_name_v', views.actor_name_vViewSet)
router.register(r'actor', views.actors_vViewSet)
router.register(r'add_colom', views.add_colom_vViewSet)
router.register(r'all_film_actors', views.all_actors_film_vViewSet)
router.register(r'all_end_gen', views.all_end_gen_vViewSet)
router.register(r'all_end_li', views.all_end_li_vViewSet)
router.register(r'count_last_least', views.count_last_least_vViewSet)
router.register(r'count_last', views.count_last_vViewSet)
router.register(r'country_id', views.country_id_vViewSet)
router.register(r'customer_pay', views.customer_pay_vViewSet)
router.register(r'email', views.email_vViewSet)
router.register(r'name_address', views.f_l_add_vViewSet)
router.register(r'film_number', views.film_number_vViewSet)
router.register(r'frequently', views.frequently_vViewSet)
router.register(r'joe_data', views.joe_data_vViewSet)
router.register(r'music', views.music_kris_vViewSet)
router.register(r'store_bus', views.store_business_vViewSet)
router.register(r'store_id', views.store_id_vViewSet)
router.register(r'tp_five', views.top_five_vViewSet)
router.register(r'total_amount', views.total_amount_rung_vViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
]
